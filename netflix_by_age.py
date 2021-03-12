import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
#read edited data in
filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
input = pd.read_csv(filename)
data = np.array(input)
print(data[0,:])

#look for items that are on netflix and classify them based on age group
netflix_data = []
targets = []
for i in data:
    #print(i[6])
    if(i[6] == 1):
        if(i[3] == '7+'):
            netflix_data.append(i)
            targets.append(1)
        elif(i[3] == '13+'):
            netflix_data.append(i)
            targets.append(2)
        elif(i[3] == '18+'):
            netflix_data.append(i)
            targets.append(3)
        else:
            netflix_data.append(i)
            targets.append(i[3])
        #print(targets[-1])

netflix_data = np.array(netflix_data)
targets = np.array(targets)
print(data.shape)
print(netflix_data.shape)
print(targets.shape)

filepath = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\netflix_age_groups.csv"
pd.DataFrame(netflix_data).to_csv(filepath)

print("done")