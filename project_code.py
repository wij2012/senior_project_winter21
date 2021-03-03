
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split 
input = pd.read_csv(r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\MoviesOnStreamingPlatforms_updated.csv\MoviesOnStreamingPlatforms_updated.csv") 
# Preview the first 5 lines of the loaded data 
#print(input.head())

#convert data into a np array to allow use of np functions
input = np.array(input)
print(input[0,:])

#this is the data in each column after loading it from the .csv file
#0 row index
#1 unique movie ID
#2 Movie title
#3 Year movie was produced
#4 target age group
#5 IMDB rating out of 10
#6 Rotten Tomatoes rating %
#7 Is it on Netflix
#8 Is it on Hulu
#9 Is it on Prime Video
#10 Is it on Disney+
#11 is it a movie or tv show?
#12 who are directors?
#13 what genres does it fall under
#14 where was it produced (countries)
#15 what languages is it available in?
#16 runtime in minutes

#delete unnecessary columns of data to allow for faster processing
delete_column_at_these_indicies = [0, 1, 11, 13, 14, 15]
data = np.delete(input, obj=delete_column_at_these_indicies, axis=1)
print(len(data[0]))
print(data[0,:])

training_data, testing_data = train_test_split(data, train_size=.7, test_size=.3)
#print(training_data[:3,:])
#np.savetxt("training_data.txt", training_data, delimiter="#")
#print(testing_data[0,:])