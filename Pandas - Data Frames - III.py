#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
from numpy.random import randn


# ### Multi-level Indexed DataFrame

# In[28]:


a = ['Z1','Z1','Z1','Z0','Z0','Z0']
b = [1,2,4,1,2,4]
hierarchical_index = list(zip(a,b))#here we are creating a list of tuples using zip function along with the list function
hierarchical_index = pd.MultiIndex.from_tuples(hierarchical_index)#and the list above is used to make a MultiIndex here from tuples


# In[29]:


hierarchical_index


# In[30]:


#we are creating a multi-level_index DataFrame with columns A and B and rows Z1 and Z0 with sub-rows 1,2,4 
df = pd.DataFrame(randn(6,2),hierarchical_index,['A','B'])


# In[31]:


df


# In[32]:


#fetching data from multi-level index in data frame
#fetching everything under index Z1
df.loc['Z1']


# In[38]:


#to fetch data on the basis of sub-indexes we need to start from main index and then loc on sub-index as:
df.loc['Z1'].loc[1]


# In[40]:


#naming the index
df.index.names = ['main','sub']


# In[41]:


df


# In[42]:


#fetching any particular value from the dataframe say Z0-2-B
df.loc['Z0'].loc[2]['B']


# In[43]:


#cross section of a dataframe
df.xs('Z1')


# In[46]:


#fetching a cross-section of a dataframe on the basis of level of index
df.xs(1,level='sub')


# In[ ]:




