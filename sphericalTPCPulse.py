#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Spherical TPC Problem


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import math as mt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[40]:




Pulse=lambda V0,Ra,Rc,u,t,e:e*(V0/((1/Ra)-(1/Rc)))*((3*u*V0/((1/Ra)-(1/Rc))*t+(Ra)**(3))**(-1/3)-(1/Rc))


# In[57]:


time=np.arange(0,100,0.1)

IonPulse=[]
ePulse=[]
for i in time:
    if(i==0):
        IonPulse.append(0)
        ePulse.append(0)
    else:
        IonPulse.append(Pulse(100,0.3,5/2,0.03/1000,i,1))
        ePulse.append(Pulse(100,0.3,5/2,0.03,i,1))


# In[58]:



plt.title("Ion Pulse From Spherical TPC ")
plt.plot(time,IonPulse,alpha=1,label="ions",color="r")

#ax.set_yscale('log')
# ax.set_yscale('log')
plt.semilogy()
#plt.yscale('symlog')
plt.legend(loc='upper right')
plt.ylabel('Voltage (V)')
plt.xlabel("Time(us)")
plt.show()


plt.title("Electron Pulse From Spherical TPC ")
plt.plot(time,ePulse,alpha=1,label="e-",color="g")

#ax.set_yscale('log')
plt.yscale('symlog')
plt.semilogy()

plt.legend(loc='upper right')
plt.ylabel('Voltage (V)')
plt.xlabel("Time(us)")
plt.show()

