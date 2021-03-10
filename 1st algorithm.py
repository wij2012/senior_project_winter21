import pandas as pd
import numpy as np 

#read edited data in
filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
input = pd.read_csv(filename)
data = np.array(input)

#look for items that are on netflix and classify them based on age group
targets = []
for i in data:
    if(i[6] == 1):
        if(i[4] == '7+'):
            targets.append(1)
        elif(i[4] == '13+'):
            targets.append(2)
        elif(i[4] == '18+'):
            targets.append(3)