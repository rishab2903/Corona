#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import folium
sf_map = folium.Map(location=[0,0])
df = pd.read_csv(r'C:\Users\adi3m\Desktop\data viz\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports\03-31-2020.csv')
df = df[['Lat','Long_','Confirmed','Deaths']]
df = df.dropna(axis=0)

df = df[(df['Lat']!=0) & (df['Long_']!=0)]
df.shape
   for lat, lng, case, deaths in zip(df.Lat, df.Long_, df.Confirmed, df.Deaths):
    folium.CircleMarker(location = [lat,lng], radius=(case/10000), color='red', fill=True, fill_color='red', fill_opacity=0.6,
                       popup = {'Confirmed' : case, 'Deaths' : deaths}).add_to(sf_map)
sf_map


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[38]:


get_ipython().system('pip install folium')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:


dfnew = df.groupby('Country_Region')['Confirmed'].sum()

dfnew.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




