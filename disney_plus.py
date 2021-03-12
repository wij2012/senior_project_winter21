import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
#read edited data in
filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
input = pd.read_csv(filename)
data = np.array(input)
print(data[0,:])

#look for items that are on disney_plus and classify them based on age group
disney_plus_data = []
targets = []
for i in data:
    #print(i[6])
    if(i[9] == 1):
        if(i[3] == '7+'):
            disney_plus_data.append(i)
            targets.append(1)
        elif(i[3] == '13+'):
            disney_plus_data.append(i)
            targets.append(2)
        elif(i[3] == '18+'):
            disney_plus_data.append(i)
            targets.append(3)
        else:
            disney_plus_data.append(i)
            targets.append(i[3])
        #print(targets[-1])

disney_plus_data = np.array(disney_plus_data)
targets = np.array(targets)
print(data.shape)
print(disney_plus_data.shape)
print(targets.shape)

filepath = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\disney_plus_age_groups.csv"
pd.DataFrame(disney_plus_data).to_csv(filepath)

print("done")