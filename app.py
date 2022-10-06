#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st


# In[8]:


import pandas as pd


# In[9]:


import plotly.express as px
from PIL import Image


# In[10]:


st.set_page_config(page_title="Survey Results")
st.header("Survey Results 2021")
st.subheader("was it helpful")


# In[14]:


excel_file= "C:\\Users\\mahima neema\\Desktop\\Excel_Webapp\\Survey_Results.xlsx"
sheet_name="DATA"


# In[16]:


df=pd.read_excel(excel_file,sheet_name=sheet_name, usecols='B:D',header=3)


# In[17]:


df_participants=pd.read_excel(excel_file, sheet_name =sheet_name, usecols='F:G', header=3)


# In[23]:


df_participants.dropna(inplace=True)


# In[30]:


department=df["Department"].unique().tolist()


# In[31]:


ages=df["Age"].unique().tolist()


# In[32]:


age_selection=st.slider("Age", min_value=min(ages),max_value=max(ages), value=(min(ages),max(ages)))


# In[33]:


department_selection=st.multiselect('Department:',department,default=department)


# In[34]:


mask=(df["Age"].between(*age_selection)) & (df["Department"].isin(department_selection))


# In[35]:


number_of_results=df[mask].shape[0]


# In[ ]:


st.markdown(f"*Available Results: {number_of_results}*")


# In[36]:


df_grouped=df[mask].groupby(by=['Rating']).count()[["Age"]]


# In[38]:


df_grouped=df_grouped.rename(columns={'Age':'Votes'})


# In[39]:


df_grouped=df_grouped.reset_index()


# In[40]:


bar_chart =px.bar(df_grouped,x="Rating",y="Votes", text="Votes", color_discrete_sequence=["#F63366"]*len(df_grouped),template='plotly_white')


# In[41]:


st.plotly_chart(bar_chart)


# In[45]:


col1, col2=st.beta_columns(2)


# In[46]:


image= Image.open("C:\\Users\\mahima neema\\Desktop\\Excel_Webapp\\image\\ml.png")


# In[47]:


col1.image(image,caption="Machine Learning Models",use_column_width=True)


# In[49]:


col2.dataframe(df[mask])


# In[25]:


st.dataframe(df_participants)


# In[26]:


pie_chart = px.pie(df_participants, title="Total No of Participants",values="Participants", names="Departments")


# In[27]:


st.plotly_chart(pie_chart)

