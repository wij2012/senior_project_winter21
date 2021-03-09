import pandas as pd
import numpy as np 

filename = "edited_data.txt"
#input = pd.read_csv(filename)
#data = np.loadtxt(filename, dtype=np.string_, delimiter="||", encoding="utf-8")
data = []
with open(filename, 'r', encoding="utf-8") as f:
    for line in f.readlines():
        data.append(line.split(' '))
print(data[0,:])