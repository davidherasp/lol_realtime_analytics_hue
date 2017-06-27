
# coding: utf-8

# In[1]:

from pymongo import MongoClient


# In[2]:

client = MongoClient('mongodb://user:password@ds133932.mlab.com:33932/lol_livestats')


# In[3]:

db = client.lol_livestats


# In[10]:

g1 = db["ROCvsFNC_G1_15-06-17"]
g2 = db["ROCvsFNC_G2_15-06-17"]
g3 = db["ROCvsFNC_G3_15-06-17"]


# In[6]:

import pprint


# In[12]:

pprint.pprint(g1.find_one())


# In[13]:

g1_data = g1.find()
g2_data = g2.find()
g3_data = g3.find()


# In[18]:

for obj in g1_data:
    pprint.pprint(obj[1])


# In[ ]:



