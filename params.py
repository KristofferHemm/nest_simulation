import pandas as pd
import numpy as np
import json

ts = np.array([10, 15, 19])
tm = np.array([185, 190, 195])
th = np.array([0.5, 5.0, 10.0])

placeholder = []

for i in ts:
    for j in tm:
        for k in th:
            placeholder.append(np.array([i, j, k]))

df1 = pd.DataFrame(placeholder, columns=['tauSyn', 'tauMem', 'theta'])
df = pd.DataFrame()
for i in range(5):
    df = df.append(df1, ignore_index=True)

seed = []
for i in range(5):
    for j in range(len(df1)):
        seed.append(1234 + 123 * i)

df['seed'] = seed

df.to_csv('params.csv', index=False)

