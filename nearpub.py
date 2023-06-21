import streamlit as st
import pandas as pd
import os
import numpy as np
import plotly.express as px
st.markdown("<h1 style='text-align:center;'>Nearest Pub</h1>",unsafe_allow_html=True)

latitude=st.number_input("latitude")
longitude=st.number_input("longitude")
button=st.button("submit")

file_dir=os.path.dirname(os.path.abspath(__file__))


parent_dir=os.path.join(file_dir,os.pardir)

dir_of_interest=os.path.join(parent_dir,"resources")


data_path=os.path.join(dir_of_interest,"data","cleanpub copy.csv")

df=pd.read_csv(data_path)
df=df.drop(["Unnamed: 0"],axis=1)
n=df[["latitude","longitude"]]
new=np.array([latitude,longitude])
distances=np.sqrt(np.sum((new-n)**2,axis=1))

n=5
min_indices=np.argpartition(distances,n-1)[:n]
if button:
    st.dataframe(df.iloc[min_indices,2])
    st.text("minimum distances:")
    st.map(df.iloc[min_indices],use_container_width=True)
    st.dataframe(distances["address"].head(5))