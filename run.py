import subprocess
import pickle
import json
import os
import pandas as pd
import pyarrow.parquet as pq
from concurrent.futures import ProcessPoolExecutor

def run_brunel(params_dict):
    """
    Run the simulation in NEST
    Make sure that the number of cores is set equal to max_workers 
    Make sure that the NEST script is correct
    """
    subprocess.run(['srun', '-c', '4', 'python', 'brunel_alpha_nest.py', f'{params_dict}'])
    return f'{params_dict}'

def main():
    results = {} # dictionary for holding results
    params_df = pd.read_csv('.../params.csv') # read parameters
    params_dict = params_df.to_dict(orient='records') #transform parameters to dictionary

    with ProcessPoolExecutor(max_workers=4) as executor: # max workers must equal cpus per task in run.slurm
        for params in executor.map(run_brunel, params_dict): # run simulation for each set of parameters provided
            json_acceptable_string = params.replace("'", "\"") 
            param = json.loads(json_acceptable_string) # parameters must be in json format for the NEST script
            new_tauSyn, new_tauMem, new_theta, new_seed =  param.values()
            fname = f'ban_{new_tauSyn}_{new_tauMem}_{new_theta}_{new_seed}.parquet' # filename for each individual simulation
            table = pq.read_table(fname) # save the results returned from the simulation
            results[params] = table # save results in results dictionary
            print('.', end='')

    # Pickle the data dictionary using the highest protocol available
    with open('ban_all.pickle', 'wb') as f:
        experiment = {'parameters': params_df, 'results': results}
        pickle.dump(experiment, f, pickle.HIGHEST_PROTOCOL)
    
    # Remove parquet files after all data have been pickled
    if os.path.isfile('ban_all.pickle'):
        dir_name = os.getcwd()
        test = os.listdir(dir_name)

        for item in test:
            if item.endswith(".parquet"):
                os.remove(os.path.join(dir_name, item))
    
if __name__ == '__main__':
    main()
