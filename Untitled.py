#!/usr/bin/env python
# coding: utf-8

# **Fiz220 dersi için ilk uygulama dersi.**

# *Ekranda boş bir yere tıklarak H tuşuna basdığımızda kısa yol ve komut yardım penceresi açılır.
# Kullandığımız kütüphaneler "numpy, scipy, matpltlib, pandas."*

# In[39]:


3+7


# In[40]:


a=5


# In[41]:


a


# In[42]:


pi


# In[ ]:


import numpy as np


# *numpy kütüphanesini içeri aktarır.*

# In[ ]:


pi


# In[ ]:


np.pi


# 

# In[ ]:


a=np.matrix("1 2 3 ; 4 5 6")


# In[ ]:


a


# In[ ]:


b=np.array([[1,2,3],[4,5,6]])
b


# *satırlar ve sütunları sayarken octave'dan farklı olarak sıfırdan başlanarak sayılır.*

# In[ ]:


b[1,2]


# In[ ]:


b[1,0:2]


# In[ ]:


b[1,0:3]


# *1 satırdaki ifadelerin 0 dan 3. sütuna kadar (3 dahil değil) çağırır.*

# In[53]:


p=np.pi
print(p)
print("%.5f\n" % p,end="*")
print(5)


# In[65]:


z=np.array([[5,6,],[8,9,]])
z


# In[67]:


print("%d/%d:%d/%d"%(z[0,0],z[0,1],[1,0],[1,1]))


# In[68]:


furkan="akkaya"
print(furkan)


# In[ ]:




