#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CREATING THE YEARS AND DURATION DATAFRAME
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

#DICTIONARY WITH THE TWO
movie_dict={'years':years, 'durations':durations}
movie_dict


# In[3]:


# # Import pandas 
import pandas as pd

# Create a DataFrame from the dictionary
durations_dataframe = pd.DataFrame(movie_dict)

# Print the DataFrame
print(durations_dataframe)


# In[3]:


$ ipython locate


# In[4]:


#VISUALIZATION
# We will use a line chart to visualize year of release against duration

#import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()

#Drawing a line plot
plt.plot(durations_dataframe['years'],durations_dataframe['durations'])
plt.title("Netflix Movie duration against year of release")
#show the plot
plt.show()


# In[11]:


#read the csv as a dataframe
import pandas as pd
import numpy as np
netflix_df=pd.read_csv("netflix_data1.csv")
netflix_df

print(netflix_df[0:5])


# In[12]:


netflix_movies_only=netflix_df[netflix_df['type'] == 'Movie']
netflix_movies_only
#select only the columns of interest


# In[19]:


netflix_movies_col_subset = netflix_movies_only[['title', 'country','genre','release_year','duration']]
netflix_movies_col_subset


# In[21]:


#create a figure and increase the figure size
fig=plt.figure(figsize=(12,8))

#create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset["release_year"],netflix_movies_col_subset["duration"])

#create a title
plt.title("Movie duration by year of release")

