#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:06:45 2020

@author: aimsd
"""

import numpy as np

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re


# In[ ]:


labels = pd.read_csv("/home/aims/Downloads/data/attributes/attributes/labels.txt",
                     delimiter=" ",names=["image_id", "attribute_id" , "is_present", "certainty_id", "worker_id"])
attributes = pd.read_csv("/home/aims/Downloads/data/attributes/attributes/attributes.txt", delimiter=" ",names=["attr_id","Attribute"])
certeinties = pd.read_csv("/home/aims/Downloads/data/attributes/attributes/certainties.txt", delimiter=" ",names=["certainty_id","certainty"])

def replace(x):
    x = re.sub("[_]"," ",x)
    x = re.sub("::"," ",x)
    return x
    


# In[ ]:


attributes["Attribute"]=attributes["Attribute"].apply(lambda x:replace(x))


# In[ ]:


attributes


# In[ ]:


j = 0
all_features =[]
for i in range(10):
    img_id = labels.iloc[j]["image_id"]
    features = set()
    while labels.iloc[j]["image_id"]==img_id:
        attr_id = labels.iloc[j]["attribute_id"]
        attr = attributes[attributes["attr_id"]==attr_id]["Attribute"].values[0]
        present = labels.iloc[j]["is_present"]
        certainty_id = labels.iloc[j]["certainty_id"]
        if present==0:
            j+=1
            continue
        #print(type(certainty_id))
        certainty = certeinties[certeinties["certainty_id"]==int(certainty_id)]["certainty"].values[0]
        #print(certainty)
        features.add((certainty.lower()+" "+attr))
        j+=1
    print(j)
    all_features.append(features)
    


# In[ ]:


#certeinties[certeinties["certainty_id"]==2]["certainty"].values[0]


# In[ ]:


all_features


# In[ ]:


s = " ".join(features)


# In[ ]:


s


# In[ ]:




