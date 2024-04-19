import pandas as pd
import numpy as np

ts = np.array([10, 15, 19]) # synaptic time constant 
tm = np.array([185, 190, 195]) # time constant of membrane potential in ms
th = np.array([0.5, 5.0, 10.0]) # spike threshold

paramslist = []

# Creating nested lists for all parameter combinations
for i in ts:
    for j in tm:
        for k in th:
            paramslist.append(np.array([i, j, k]))

# Place all parameter combinations in a datafram
df_noseed = pd.DataFrame(paramslist, columns=['tauSyn', 'tauMem', 'theta'])

# Stack the noseed dataframe 5 times to prepare simulations using 5 different seeds
df_seed = pd.DataFrame()
for i in range(5):
    df_seed = df_seed.append(df_noseed, ignore_index=True)

# Create list of seeds in increments of 123
seed = []
for i in range(5):
    for j in range(len(df_noseed)):
        seed.append(1234 + 123 * i)

# Insert seeds into the dataframe
df_seed['seed'] = seed

# Save dataframe as csv file
df_seed.to_csv('params.csv', index=False)

