#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x = np.array([1000,1500,2000,2500,3000]).reshape(-1,1)  # size


# In[10]:


y = np.array([200000,250000,280000,310000,350000]) # price


# In[11]:


model = LinearRegression() 
model.fit(x,y)


# In[20]:


predicted_price = model.predict([[2200]])


# In[18]:


print(predicted_price)


# In[ ]:





# In[ ]:





# In[19]:


print(f"Predicted Price: ${predicted_price[0]: .2f}")


# In[22]:


plt.scatter(x,y,color= "blue", label= "Regression Line")
plt.plot(x,model.predict(x), color= 'red',label = 'Regression Line')
plt.xlabel("Size(sq ft)")
plt.ylabel("Price($)")
plt.legend()
plt.title("Linear regression Example")


# In[24]:


print(f"Slope (Coefficient): {model.coef_[0]:,.2f}")


# In[ ]:




