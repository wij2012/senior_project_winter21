#here we go
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split

def prep_data():
    filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
    input = pd.read_csv(filename)
    data = pd.DataFrame(input)
    print("before")
    print(data.loc[[0]])
    data = data.drop(data.columns[[0]], axis=1)
    
    print("after")
    print(data.loc[[0]])
    
    data.columns = ["title", "year", "age_group", "imdb", "rotten_tomatoes", "netflix", "hulu", "prime video", "disney+", "director(s)", "runtime"]
    print(data.loc[[0]])
    #data = np.array(input)
    #print(data[0,:])

prep_data()