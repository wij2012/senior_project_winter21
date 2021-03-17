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
    
    data.columns = ["title", "year", "age_group", "imdb", "rotten_tomatoes", "netflix", "hulu", "prime_video", "disney_plus", "director", "runtime"]
    print(data.loc[[0]])
    #data = np.array(input)
    #print(data[0,:])

    data.title.fillna("unknown")
    data.year.fillna("unknown")
    data.age_group.fillna("unknown")
    data.imdb.fillna("unknown")
    data.rotten_tomatoes.fillna("unknown")
    data.netflix.fillna("unknown")
    data.hulu.fillna("unknown")
    data.prime_video.fillna("unknown")
    data.disney_plus.fillna("unknown")
    data.director.fillna("unknown")
    data.runtime.fillna("unknown")

prep_data()