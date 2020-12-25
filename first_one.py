#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns 

#Remove Warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("The Job Seekers in Kerala")

#import dataset
df_job_seekers = pd.read_csv('Educational_Breakup.csv',skiprows = 2)
df_job_seekers = df_job_seekers.dropna()
df_job_seekers = df_job_seekers.drop(df_job_seekers.columns[[0]], axis = 1)
df_job_seekers = df_job_seekers.rename(columns=lambda x: x.strip())

df_job_seekers['total_jobseekers'] = df_job_seekers['Male'] + df_job_seekers['Female']


#Display the table
st.header("The data set")
#st.table(df_job_seekers)
st.write("This is the data of Educational wise Break up of jobseekers registered with Employment Exchanges in Kerala as on 31/10/2019. \
    \nThe dataset can be accessed [here](https://kerala.data.gov.in/catalog/educational-wise-break-jobseekers-registered-employment-exchanges-kerala).")

st.header("Insights into the data")
#bar plot
st.subheader("Total Number of Job seekers in Kerala, District wise")
ax = sns.barplot(x='Districts',y='total_jobseekers',orient="v", data=df_job_seekers)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
st.pyplot()

#bar plot
st.subheader("Total Number of Post Graduate Job Seekers in Kerala, District wise")
ax = sns.barplot(x='Districts',y='Post Graduate',orient="v", data=df_job_seekers)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
st.pyplot()

st.subheader("Total Number of Graduate Job Seekers in Kerala, District wise")
ax = sns.barplot(x='Districts',y='Graduate',orient="v", data=df_job_seekers)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
st.pyplot()

#bar plot
sns.set_theme(style="ticks")
st.subheader("Total Number of  Matric Job Seekers in Kerala, District wise")
ax = sns.barplot(x='Districts',y='Matric',orient="v", data=df_job_seekers)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
st.pyplot()

#bar plot
st.subheader("Total Number of Below Matric Job Seekers in Kerala, District wise")
ax = sns.barplot(x='Districts',y='Below Matric',orient="v", data=df_job_seekers)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
st.pyplot()

#bar plot
st.subheader("Total Number of Illiterate Job Seekers in Kerala, District wise")
ax = sns.barplot(x='Districts',y='Illiterates',orient="v", data=df_job_seekers)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
st.pyplot()

