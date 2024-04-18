import subprocess
import pickle
import json
import os
import pandas as pd
import pyarrow.parquet as pq
from concurrent.futures import ProcessPoolExecutor

def run_brunel(params_dict):
    subprocess.run(['srun', '-c', '4', 'python', 'brunel_alpha_nest.py', f'{params_dict}'])
    return f'{params_dict}'

def main():
    results = {}
    params_df = pd.read_csv('.../params.csv')
    params_dict = params_df.to_dict(orient='records')

    with ProcessPoolExecutor(max_workers=4) as executor:
        for params in executor.map(run_brunel, params_dict):
            json_acceptable_string = params.replace("'", "\"")
            param = json.loads(json_acceptable_string)
            new_tauSyn, new_tauMem, new_theta, new_seed =  param.values()
            fname = f'ban_{new_tauSyn}_{new_tauMem}_{new_theta}_{new_seed}.parquet'
            table = pq.read_table(fname)
            results[params] = table
            print('.', end='')


    with open('ban_all.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        experiment = {'parameters': params_df, 'results': results}
        pickle.dump(experiment, f, pickle.HIGHEST_PROTOCOL)
    
    # Slette parquet filer
    if os.path.isfile('ban_all.pickle'):
        dir_name = os.getcwd()
        test = os.listdir(dir_name)

        for item in test:
            if item.endswith(".parquet"):
                os.remove(os.path.join(dir_name, item))
    
if __name__ == '__main__':
    main()
