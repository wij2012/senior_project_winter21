#here we go
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split

def prep_data():
    filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
    input = pd.read_csv(filename)
    data = pd.DataFrame(input)
    #print("before")
    #print(data.loc[[0]])
    data = data.drop(data.columns[[0]], axis=1)
    
    #print("after")
    #print(data.loc[[0]])
    
    data.columns = ["title", "year", "age_group", "imdb", "rotten_tomatoes", "netflix", 
    "hulu", "prime_video", "disney_plus", "director", "runtime"]
    print(data.loc[[0]])
    #data = np.array(input)
    #print(data[0,:])

    #fill empty data slots with unknown for consistency
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

    titles = data.title
    years = data.year
    directors = data.director
    runtimes = data.runtime
    data = data.drop(data.columns[[0, 1, 9, 10]], axis=1)

    print(data.loc[[0]])

    
    """ #create new dataframe with number values
    data_new = pd.get_dummies(data, columns=["title", "year", "age_group", "imdb", "rotten_tomatoes", 
    "netflix", "hulu", "prime_video", "disney_plus", "director", "runtime"])

    data_new.title = data.title.astype("title")
    data_new["title_codes"] = data_new.title.cat.codes

    data_new.year = data.year.astype("year")
    data_new["year_codes"] = data_new.year.cat.codes

    data_new.age_group = data.age_group.astype("age_group")
    data_new["age_group_codes"] = data_new.age_group.cat.codes
    
    data_new.imdb = data.imdb.astype("imdb")
    data_new["imdb_codes"] = data_new.imdb.cat.codes

    data_new.rotten_tomatoes = data.rotten_tomatoes.astype("rotten_tomatoes")
    data_new["rotten_tomatoes_codes"] = data_new.rotten_tomatoes.cat.codes

    data_new.netflix = data.netflix.astype("netflix")
    data_new["netflix_codes"] = data_new.netflix.cat.codes

    data_new.hulu = data.hulu.astype("hulu")
    data_new["hulu_codes"] = data_new.hulu.cat.codes

    data_new.prime_video = data.prime_video.astype("prime_video")
    data_new["prime_video_codes"] = data_new.prime_video.cat.codes

    data_new.disney_plus = data.disney_plus.astype("disney_plus")
    data_new["disney_plus_codes"] = data_new.disney_plus.cat.codes

    data_new.director = data.director.astype("director")
    data_new["director_codes"] = data_new.director.cat.codes

    data_new.runtime = data.runtime.astype("runtime")
    data_new["runtime_codes"] = data_new.runtime.cat.codes """

prep_data()
