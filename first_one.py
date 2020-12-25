#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Educational wise Break up of jobseekers registered with Employment Exchanges in Kerala as on 31/10/2019")

#import dataset
df_job_seekers = pd.read_csv('Educational_Breakup.csv',skiprows = 2)
df_job_seekers = df_job_seekers.dropna()
df_job_seekers = df_job_seekers.drop(df_job_seekers.columns[[0]], axis = 1)
df_job_seekers = df_job_seekers.rename(columns=lambda x: x.strip())
#display the data-set
df_job_seekers.head(14)
#Display the table
st.table(df_job_seekers)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
df_job_seekers.plot(kind='bar')
st.pyplot()
# ax = sns.barplot(x='Districts',y='Male',orient="v", data=df_job_seekers)

# ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# #Displot
# st.subheader("Displot")
# st.pyplot()

# tips = sns.load_dataset("tips")

# sns.displot(data=tips, x="total_bill", hue="tip")


# sns.displot(data=df_job_seekers, x="Matric", hue="Districts")


# #joinplot
# st.subheader("JointPlot")
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
# st.pyplot()
# #pairplot
# st.subheader("Pairplot")
# sns.pairplot(tips,hue='sex',palette='rainbow')
# st.pyplot()
# #Rugplot
# st.subheader("Rugplot")
# sns.rugplot(tips['tip'])
# st.pyplot()
# #Correation
# st.subheader("Heatmap")
# sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
# st.pyplot()
