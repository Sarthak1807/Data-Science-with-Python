#!/usr/bin/env python
# coding: utf-8

# # Weather Data Visualization using Python 
# ## By Sarthak Sarode

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)


# In[3]:


weather = pd.read_csv('Test.csv')
weather


# In[4]:


weather.info()


# In[5]:


sns.barplot(weather['humidity'],weather['temperature'])



# In[6]:


sns.distplot(weather['humidity'])


# In[7]:


sns.jointplot(weather['humidity'],weather['temperature'])


# In[9]:


sns.jointplot(weather['humidity'],weather['temperature'],kind="hex")


# In[10]:


sns.jointplot(weather['humidity'],weather['temperature'],kind="kde")


# In[11]:


sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])


# In[12]:


sns.stripplot(weather['weather_type'],weather['temperature'])


# In[14]:


sns.countplot(x="weather_type", data=weather)


# In[15]:


sns.countplot(x="weather_description", data=weather)


# In[16]:


sns.stripplot(weather['weather_type'],weather['temperature'],jitter=True)


# In[17]:


sns.boxplot(weather['humidity'],weather['temperature'],hue=weather['weather_type'])


# In[18]:


sns.barplot(weather['humidity'],weather['temperature'],hue=weather['weather_type'])


# In[19]:


sns.pointplot(weather['humidity'],weather['temperature'],hue=weather['weather_type'])


# In[20]:


sns.lmplot(x="humidity",y="temperature",data=weather)


# In[31]:


sns.lmplot(x="humidity", y="temperature", hue="weather_type", data=weather)
plt.savefig("figure.png")


# In[32]:


weather['weather_type'].value_counts()


# In[34]:


weather['weather_type'].value_counts(ascending=True)


# In[33]:


weather['weather_description'].value_counts()


# In[36]:


weather['weather_description'].value_counts(ascending=True)


# In[38]:


weather['air_pollution_index'].describe()


# In[39]:


weather['humidity'].describe()


# In[40]:


weather['temperature'].describe()


# In[ ]:




