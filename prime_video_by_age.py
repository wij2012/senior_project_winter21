import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
#read edited data in
filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
input = pd.read_csv(filename)
data = np.array(input)
print(data[0,:])

#look for items that are on prime_video and classify them based on age group
prime_video_data = []
targets = []
for i in data:
    #print(i[6])
    if(i[8] == 1):
        if(i[3] == '7+'):
            prime_video_data.append(i)
            targets.append(1)
        elif(i[3] == '13+'):
            prime_video_data.append(i)
            targets.append(2)
        elif(i[3] == '18+'):
            prime_video_data.append(i)
            targets.append(3)
        else:
            prime_video_data.append(i)
            targets.append(i[3])
        #print(targets[-1])

prime_video_data = np.array(prime_video_data)
targets = np.array(targets)
print(data.shape)
print(prime_video_data.shape)
print(targets.shape)

filepath = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\prime_video_age_groups.csv"
pd.DataFrame(prime_video_data).to_csv(filepath)

print("done")