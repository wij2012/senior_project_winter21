#here we go
import pandas as pd
import numpy as np 
import math
from sklearn.model_selection import train_test_split

def prep_data():

    #read rata in from given file path and create a pandas dataframe from it
    filename = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
    input = pd.read_csv(filename)

    """ average_ratings = []

    count = 0
    for i in input:
        print("count: ", count)
        print(i[4], i[5])
        average = ((float(i[4]) * 10) * float(i[5])) / 2
        average_ratings.append(average)
        count += 1  """

    data = pd.DataFrame(input)
    #print("before")
    #print(data.loc[[0]])
    data = data.drop(data.columns[[0]], axis=1)
    
    #print("after")
    #print(data.loc[[0]])
    
    #give the columns in the dataframe names
    data.columns = ["title", "year", "age_group", "imdb", "rotten_tomatoes", "netflix", 
    "hulu", "prime_video", "disney_plus", "director", "runtime"]
    print(data.loc[[0]])

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

    print(data.loc[[0]])

    ratings_only = data[["imdb", "rotten_tomatoes"]]

    average_ratings = []
    count = 0

    for i in data.index:
        #print(data["imdb"][i], data["rotten_tomatoes"][i])

        #create temporary variables to hold the values of imdb and rotten tomatoes at this index
        imdb_temp = data["imdb"][i]
        rotten_temp = data["rotten_tomatoes"][i]

        #handle the % in the rotten tomatoes column and the blank entries
        if('%' in str(rotten_temp)):
            rotten_temp = rotten_temp[:-1:]
        else:
            rotten_temp = -1
        
        #handle blank entries in imdb
        if(math.isnan(imdb_temp)):
            imdb_temp = -1

        #calculate the average between the two ratings
        #note if either rating is zero, set average to the other rating
        #if both are zero set average to -1 (disregard)
        average = -1
        if((imdb_temp != -1) and (rotten_temp != -1)):
            average = ((imdb_temp * 10.0) * float(rotten_temp)) / 2.0
        elif((imdb_temp != -1) and (float(rotten_temp) == -1)):
            average = imdb_temp * 10.0
        elif((imdb_temp == -1) and (float(rotten_temp) != -1)):
            average = float(rotten_temp)
        
        average_ratings.append(average)

        #this is just to keep track of how many averages are above 100 ie wrong
        if(average > 100):
            count += 1
            #print(average)

    print(count) #count is the total number of averages that are above 100

    print(data.loc[[0]])

    #for some reason this set of commands works but the letters aren't changing colors
    """ratings = pd.DataFrame(average_ratings)
    print(ratings) """

    #separate data columns out that aren't needed for determining target values
    titles = data.title
    years = data.year
    directors = data.director
    runtimes = data.runtime
    data = data.drop(data.columns[[0, 1, 3, 4, 9, 10]], axis=1)
    
    #the 2 line comment block is doing something wierd and I think it's affecting the 
    #line below this comment
    #data = data.append(ratings)

    print(data.loc[[0]])

prep_data()
