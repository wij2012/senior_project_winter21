from sklearn.model_selection import train_test_split 
import pandas as pd
import numpy as np 
from sklearn import tree
from sklearn.metrics import accuracy_score

#read edited data in
filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
input = pd.read_csv(filename)
data = np.array(input)
print(data[0,:])

classifier = tree.DecisionTreeClassifier()

targets = []
for i in data:
    #print(i[6])
    if(i[7] == 1):
        if(i[3] == '7+'):
            targets.append(1)
        elif(i[3] == '13+'):
            targets.append(2)
        elif(i[3] == '18+'):
            targets.append(3)
        else:
            targets.append(i[3])
    else:
        targets.append(-1)
        #print(targets[-1])

targets = np.array(targets)
print(data.shape)
print(targets.shape)

data_train, data_test, targets_train, targets_test = train_test_split(data, targets, test_size = .5)
classifier.fit(data_train, targets_train)

predictions = classifier.predict(data_test)
print(accuracy_score(targets_test, predictions))