import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, 'data',"kaggle_diabetes.csv")

st.markdown("""
    <style>
        body {
            background-image: url("https://img.freepik.com/premium-photo/background-diabetic-disease-concept-with-copy-space-world-diabetes-day-banner_132254-879.jpg?w=900");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:black;'>Data Visualization</h1>",unsafe_allow_html=True)

df = pd.read_csv(DATA_PATH)

st.write(df.describe())

st.bar_chart(df["Outcome"].value_counts())

diabetes = df[df['Outcome']==1]
no_diabetes = df[df['Outcome']==0]

fig, ax = plt.subplots()
ax.scatter(diabetes['Age'], diabetes['Glucose'],c='red',alpha=0.5, label='Diabetes')
ax.scatter(no_diabetes['Age'],no_diabetes["Glucose"],c='blue' ,alpha=0.5, label='No Diabetes')
ax.set_xlabel('Age')
ax.set_ylabel("Glucose Level")
ax.legend()
st.pyplot(fig)



labels = ['Diabetic', 'Non-Diabetic']
sizes = [34.2, 65.8]
fig, ax = plt.subplots()
_, _, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Percentage of Diabetic Patients')

for autotext in autotexts:
    autotext.set_fontsize(12)

st.pyplot(fig)