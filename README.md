# nest_simulation
Simulate neural networks using NEST simulator, optimized for running many small simulations in parallel on a single compute node on the JUSUF supercomputer at Jülich Research Center.


## Description

## Dependencies
NEST simulator installed on either Linux or Mac.
For a Windows machine, NEST must be installed on a virtual machine or Windows Subsystem for Linux.

Required packages
```
concurrent.futures
numpy
pandas
parquet
pickle
pyarrow
scipy
```

## Usage
For running simulations on your local computer, use run.py to run the simulation.
The parameter settings for your simulation must be provided by a csv-file, params.csv.
params.py is provided as an example for making a csv-file that includes the parameters for a set of simulations.

The parameters that are normal to vary includes:

The network parameters
g = 6.0  # ratio inhibitory weight/excitatory weight
eta = 2.0  # external rate relative to threshold rate
epsilon = 0.1  # connection probability
order = 2500 # size of the network

The neuron parameters
"C_m": 1.0,
"tau_m": tauMem,
"t_ref": 2.0,
"E_L": 0.0,
"V_reset": 0.0,
"V_m": 0.0,
"V_th": theta,
"tau_syn_ex": tauSyn,
"tau_syn_in": tauSyn

For running simulations on a supercomputer, such as JUSUF, us run.slurm