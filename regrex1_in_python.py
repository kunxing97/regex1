#!/usr/bin/env python
# coding: utf-8

# # importing packages 

# In[22]:


import pandas as pd
import sklearn
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()


# # reading data 

# In[23]:


regrex1 = pd.read_csv("regrex1.csv")


# In[13]:


regrex1.plot.scatter(x='x',y='y', title='Scatter Plot in Python')
plt.savefig('py_orig.png')
plt.show()


# # making 1D model into 2D, splitting data into test and train 

# In[14]:


data = sklearn.linear_model.LinearRegression()
x = regrex1['x'].values.reshape(-1,1)
y = regrex1['y'].values.reshape(-1,1)
x_train = x
x_test = x
y_train = y
y_test = y


# # training the algorithm 

# In[15]:


regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
LinearRegression()


# # plot linear model with test data 

# In[16]:


plt.scatter(x_test, y_test,  color='gray')
plt.plot(x_test, y_pred, color='red', linewidth=2)
#mpl.plot()
plt.show()


# # plot linear model with original data 

# In[17]:


plt.scatter(regrex1['x'], regrex1['y'], color = 'gray')
plt.plot(x_test, y_pred, color='red', linewidth=2)
plt.savefig('py_Im.png')
plt.show()



# In[ ]:




