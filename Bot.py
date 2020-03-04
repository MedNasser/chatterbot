#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import *
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd


# In[2]:


chatbot = ChatBot('Menaps')


# In[3]:


trainer = ListTrainer(chatbot)


# In[4]:


df=pd.read_table("countries.txt",error_bad_lines=False,sep=";")


# In[5]:


df.head()


# In[6]:


tr=[]


# In[7]:


for idx,row in df.iterrows():
    tr.append("What is the capital of "+str(row["name"]).lower()+" ?")
    tr.append("the capital of "+str(row["name"]).lower()+" is "+str(row["capital"]))


# In[8]:


# Train the chatbot based on the english corpus
trainer.train(tr)


# In[ ]:




