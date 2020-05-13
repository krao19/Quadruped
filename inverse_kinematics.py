#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import *


# In[3]:



''' 
initial values of the system
'''
a1 = 6.2  
a2 = 5.2  
a3 = 0  
a4 = 7 

''' 
a1: y lenght between base and link 1
a2: length of rod 1
a3: y length between link 1 and link 2
a4: length of rod 2
''' 

# Desired Position of End effector
x = -7
y = 9

# Equations for Inverse kinematics
r1 = sqrt(x**2+y**2)  # eqn 1
phi_1 = arccos((a4**2-a2**2-r1**2)/(-2*a2*r1))  # eqn 2
phi_2 = arctan2(y, x)  # eqn 3
theta_1 = rad2deg(phi_2-phi_1)  # eqn 4 converted to degrees

phi_3 = arccos((r1**2-a2**2-a4**2)/(-2*a2*a4))
theta_2 = 180-rad2deg(phi_3)

print('theta one: ', theta_1)
print('theta two: ', theta_2)


# In[ ]:




