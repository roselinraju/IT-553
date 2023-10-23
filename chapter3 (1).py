#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


import os

directory_path = "/Users/gyan/Documents/Pythonfiles"

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    file_list = os.listdir(directory_path)
    for filename in file_list:
        print(filename)
else:
    print("The specified path is not a valid directory.")


# In[10]:


import csv


# In[11]:


import json


# In[13]:


#opens the csv file
with open('/Users/gyan/Documents/Pythonfiles/SalesJan2009.csv',"r") as f:
    reader=csv.reader(f)
    sales_data=[]
    #iterate through each line and puts value into the list in form of dictionary
    for row in reader:
        sales_data.append({'Transaction_date':row[0].strip('"'),'Product':row[1].strip('"'),'Price':row[2].strip('"')
                           ,'Payment_Type':row[3].strip('"'),'Name':row[4].strip('"'), 'City':row[5].strip('"'),'State':row[6].strip('"'),'Country':row[7].strip('"')})

#creates a json file and added data into it.
with open('transaction_data.json','w') as jsonf:
    json.dump(sales_data,jsonf, indent=4)


# In[14]:


print (sales_data)


# In[ ]:




