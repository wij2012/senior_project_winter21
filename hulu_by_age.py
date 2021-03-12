import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
#read edited data in
filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
input = pd.read_csv(filename)
data = np.array(input)
print(data[0,:])

#look for items that are on hulu and classify them based on age group
hulu_data = []
targets = []
for i in data:
    #print(i[6])
    if(i[7] == 1):
        if(i[3] == '7+'):
            hulu_data.append(i)
            targets.append(1)
        elif(i[3] == '13+'):
            hulu_data.append(i)
            targets.append(2)
        elif(i[3] == '18+'):
            hulu_data.append(i)
            targets.append(3)
        else:
            hulu_data.append(i)
            targets.append(i[3])
        #print(targets[-1])

hulu_data = np.array(hulu_data)
targets = np.array(targets)
print(data.shape)
print(hulu_data.shape)
print(targets.shape)

filepath = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\hulu_age_groups.csv"
pd.DataFrame(hulu_data).to_csv(filepath)

print("done")