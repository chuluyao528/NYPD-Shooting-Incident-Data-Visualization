#!/usr/bin/env python
# coding: utf-8

# Luyao Chu
# CIS 4170
# 
# For the final presentation on data visualization, I will be using the NYPD Shooting Incident Data from the U.S. Government Open Data. The dataset contains every shooting incident that happened in New York City starting from 2006 to the previous calendar year. It includes every shooting incident in each borough from NYC in detail, such as the location, time, suspect, and victim demographic.

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#import the csv dataset and show the head 
df=pd.read_csv("NYPD_Shooting_Incident_Data__Historic_.csv")
df.head()


# In[2]:


df.dtypes


# In[3]:


#selecting the column is going to be used in first graph
boro=df['BORO'].unique()
print(boro)


# In[4]:


#display the frequency
boro=df['BORO'].value_counts()
boro


# In[5]:


#creating a pie chart showing the shooting frequency in each borough
values=[8913,6195,3225,2647,646]
colors=['red','orange','yellow','grey','white']
labels=['Brooklyn','Bronx','Queens','Manhattan','Staten Island']

plt.pie(values,
        colors=colors,
        labels=labels,
        autopct='%1.1f%%',
        counterclock=True, 
        shadow=True)
plt.title('Shooting % in each borough')
plt.show()


# In[6]:


#selecting age group column for the bar chart
df['PERP_AGE_GROUP'].value_counts()


# In[7]:


#clean null and wrong data
perp_age = df[df['PERP_AGE_GROUP'] == '1020'].index 
df.drop(perp_age, inplace = True)
perp_age2 = df[df['PERP_AGE_GROUP'] == 'UNKNOWN'].index
df.drop(perp_age2, inplace = True)
perp_age3 = df[df['PERP_AGE_GROUP'] == '224'].index 
df.drop(perp_age3, inplace = True)
perp_age4 = df[df['PERP_AGE_GROUP'] == '940'].index 
df.drop(perp_age4, inplace = True)


# In[8]:


#dispaly the clean data
df['PERP_AGE_GROUP'].value_counts()


# 

# In[9]:


#creating a new crosstab for age group and race group
df_solution = pd.crosstab(index=df['PERP_AGE_GROUP'],columns=df['PERP_RACE'])
df_solution 


# In[10]:


#creating a stacked bar chart 
df_solution.plot.barh(stacked=True)


# In[11]:


df['OCCUR_DATE'] = pd.to_datetime(df['OCCUR_DATE'])
df['year'] = df['OCCUR_DATE'].dt.year  #create a year column 
df.groupby('year')['OCCUR_DATE'].count().plot()  #combine the year column to the dataset
#creating a line chart
plt.xlabel("Time (year)")
plt.ylabel("Number of Shooting Incidents")
ax=plt.gca()
ax.grid(True)
plt.show()


# In[12]:


#creating a new crosstab for victim information
vic_info=pd.crosstab(index=df['VIC_AGE_GROUP'],columns=df['VIC_RACE'])
vic_info


# In[13]:


ax=sns.heatmap(vic_info,annot=True,fmt="d",linewidths=.5)


# In[15]:


sus_info=pd.crosstab(index=df['PERP_AGE_GROUP'],columns=df['PERP_RACE'])
sus_info


# In[16]:


ax=sns.heatmap(sus_info,annot=True,fmt="d",linewidths=.5)

