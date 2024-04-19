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

The parameters common to vary include:

The network parameters
```
g           # ratio inhibitory weight/excitatory weight
eta         # external rate relative to threshold rate
epsilon     # connection probability
order       # determines the size of the network
```

The neuron parameters
```
C_m         # capacitance of membrane in in pF
tau_m       # time constant of membrane potential in ms
t_ref       # duration of refractory period in ms
E_L         # resting membrane potential in mV
V_reset     #reset potential of the membrane in mV
V_m         #absolute lower value for the membrane potential in mV
V_th        #spike threshold in mV
tau_syn_ex  # synaptic time constant in ms for excitatory neurons
tau_syn_in  # synaptic time constant in ms for inhibitory neurons
```

For reproducibility, do not use random seeds, but set seeds in the input parameters.
```
seed
```

For running simulations on a supercomputer, such as JUSUF, use run.slurm