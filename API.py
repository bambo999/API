#!/usr/bin/env python
# coding: utf-8

# # Application Programming Interface

# In[1]:


get_ipython().system('pip install nba_api')


# In[2]:


def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict    


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


# creating a dictionary
dict_={'a':[11,21,31],'b':[12,22,32]}


# In[5]:


df=pd.DataFrame(dict_)
type(df)


# In[6]:


df.head()


# In[7]:


df.mean()


# In[8]:


from nba_api.stats.static import teams
import matplotlib.pyplot as plt


# In[9]:


nba_teams = teams.get_teams()


# In[10]:


# The dictionary key id has a unique identifier for each team as a value, let's look at the first three elements of the list:
nba_teams[0:3]


# In[12]:


# convert the dictionary to a table. First, we use the function one dict, to create a dictionary. 
dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()


# In[13]:


# row that contains the warriors by using the column nickname as follows:
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors


# In[14]:


# access the first column of the dataframe:
id_warriors=df_warriors[['id']].values[0][0]
#we now have an integer that can be used to request the Warriors information 
id_warriors


# In[15]:


# The function "League Game Finder " will make an API call, its in the module stats.endpoints
from nba_api.stats.endpoints import leaguegamefinder


# In[16]:


# dataframe from the API call for Golden State and run the rest like a video.
get_ipython().system(' wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl')


# In[17]:


file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()


# In[28]:


# create two dataframes, one for the games that the Warriors faced the raptors at home and the second for away games.
games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']


# In[29]:


# calculate the mean for the column PLUS_MINUS for the dataframes games_home and  games_away:
games_home.mean()['PLUS_MINUS']


# In[30]:


games_away.mean()['PLUS_MINUS']


# In[31]:


# plot out the PLUS MINUS column for for the dataframes games_home and  games_away. We see the warriors played better at home.
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()


# In[ ]:




