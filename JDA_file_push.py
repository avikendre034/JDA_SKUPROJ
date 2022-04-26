#!/usr/bin/env python
# coding: utf-8

# ### JDA_SKU_file

# In[2]:


from pathlib import Path
import os
import six
import textwrap
import pyodbc
import seaborn as sns
import pandas as pd                                                             
import numpy as np                                                              
import warnings                                                                   
warnings.filterwarnings("ignore") 


# In[3]:


pyodbc.drivers()


# In[4]:



connection_str="""DRIVER={ODBC Driver 17 for SQL Server};
                  SERVER=gsc-scpat-sql-001-d.database.windows.net;
                  Database=SC-PAT-DB;
                  UID=SCPAT;
                  PWD=Ecolab@1234;"""


# In[5]:


conn = pyodbc.connect(connection_str)


# In[6]:


conn


# In[7]:


JDA_df = pd.read_sql('select top (10) * from [Plan_Data_Snap].[JDA_SKUPROJ]',con=conn)


# In[8]:


JDA_df.head()


# In[ ]:


JDA_df.to_excel(Path.cwd() / "JDA_Plan_data.xlsx", index=False)
jda_path =  Path.cwd() / "JDA_Plan_data.xlsx"
jda_destination = "C:/Users/kendrav/OneDrive - Ecolab/Projects - Pune/Plan Capture Database/Data Repository/"
dest_path = shutil.copy(jda_path,jda_destination)
print("File Copied to sharepoint path :",dest_path)


# In[ ]:





# In[ ]:





# In[ ]:




