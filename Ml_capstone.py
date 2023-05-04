#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk
from nltk.metrics import edit_distance


# In[2]:


data=pd.read_csv(r"C:\Users\REALME\Desktop\My Projects\ML projct 2\info.csv")
pd.set_option('display.max_columns', None)


# In[3]:


# function returns the count of the job as pr skills
def count_jobs(skill,city):
    result =data[(data["Skills"].isin(skill))&(data["Location"]==city)]["Skills"].count() 
    if result=="": return "NA"
    else: return result


# In[4]:


# Most common Company Class where that skill is required
def Company_Class(skill,city): 
    d=pd.DataFrame(data[(data["Skills"].isin(skill))&(data["Location"]==city)].groupby(["class"])["Skills"].count())
    d=d.sort_values(by=['Skills'],ascending=False)
    result =d.index[0]
    if result=="": return "NA"
    else:
        if result==0: return "Class 1"
        elif result==1: return "Class 2"
        elif result==2: return "Class 3"
        elif result==3: return "Class 4"


# In[5]:


#  A most common industry where that skill or multiple skills are required
def common_industry(skill,city):
    d=pd.DataFrame(data[(data["Skills"].isin(skill))&(data["Location"]==city)].groupby(["Job_Title"])["Skills"].count())
    d=d.sort_values(by=['Skills'],ascending=False)
    result =d.index[0]
    if result=="": return "NA"
    else: return result


# In[6]:


#  Most common experience level (From the Details table) for which the skill is required
def Common_experience(skill,city):
    d=pd.DataFrame(data[(data["Skills"].isin(skill))&(data["Location"]==city)].groupby(["Experience_level"])["Skills"].count())
    d=d.sort_values(by=['Skills'],ascending=False)
    result =d.index[0]
    if result=="": return "NA"
    else: return result
#     print(d)


# In[7]:


def complete(input_string):
    skills=[]
    # Get the 'word' column as a list
    word_list = data['Skills'].tolist()
    for i in input_string:
        min_distance = float('inf')
        closest_word = ""
        for word in word_list:
            distance = edit_distance(i, word[:len(i)])
            if distance < min_distance:
                min_distance = distance
                closest_word = word

        skills.append(closest_word)   
    return skills


# In[8]:


# skill=["sql"]
# city="Bangalore"


# In[9]:


# d=pd.DataFrame(data[(data["Skills"].isin(skill))&(data["Location"]==city)].groupby(["class"])["Skills"].count())
# d=d.sort_values(by=['Skills'],ascending=False)
# result =d.index[0]


# In[10]:


# d


# In[11]:


# type(result)


# In[ ]:




