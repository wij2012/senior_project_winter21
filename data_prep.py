# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
import math
file = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\MoviesOnStreamingPlatforms_updated.csv\MoviesOnStreamingPlatforms_updated.csv"
input = pd.read_csv(file) 
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

#get the average rating from the imdb and rotten tomatoes columns to combine them into one
average_ratings = []
for i in input:
    temp = i[6]
    #if % char found at the end of the rotten tomatoes rating, remove it
    print(temp)
    if(temp[-1] == '%'):
        temp = temp[:-1:] #remove last character in the string
    elif(math.isnan(float(temp))):
        temp = -1
    #if the rotten tomatoes rating is empty set it to -1
    else:
        temp = -1

    #check both ratings and set the average based on the results
    average = -1
    if(int(temp) < 0 and i[5] < 0): #if both ratings are less than 0 (non-existent)
        average = -1
    elif(int(temp) < 0 and i[5] > 0): #if rotten tomatoes is non-existent and imdb exists, set average to imdb * 10 
        average = i[5] * 10
    elif(int(temp) > 0 and i[5] < 0): # if imdb is non-existent and rotten tomatoes exists, set average to rotten tomatoes
        average = int(temp)
    else: #if both exist, set them to the same scale (out of 100) and calculate the average
        average = (int(temp) * (i[5] * 10)) / 2
    average_ratings.append(average)

print("average ratings size: ", len(average_ratings))

#delete unnecessary columns of data to allow for faster processing
delete_column_at_these_indicies = [0, 1, 5, 6, 11, 13, 14, 15]
data = np.delete(input, obj=delete_column_at_these_indicies, axis=1)
#print(len(data[0]))
print(data[0,:])

#write full edited data to .txt document for later use
head = "This is the beginning of the edited data"
foot = "This is the end of the edited data"
#with open("edited_data.txt") as file:
filepath = r"C:\Users\wij20\OneDrive\Desktop\School\senior_project\senior_project_winter21\edited_data.csv"
#np.savetxt(file, data, fmt='%s', delimiter=" || ", header=head, footer=foot, encoding="utf-8")
pd.DataFrame(data).to_csv(filepath)

print("done")