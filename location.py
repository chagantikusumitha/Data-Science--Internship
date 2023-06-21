import streamlit as st
import pandas as pd
import os

from matplotlib import image
st.markdown("<h1 style='text-align:center;'>pub locations</h1>",unsafe_allow_html=True)
file_dir=os.path.dirname(os.path.abspath(__file__))


parent_dir=os.path.join(file_dir,os.pardir)

dir_of_interest=os.path.join(parent_dir,"resources")


data_path=os.path.join(dir_of_interest,"data","cleanpub copy.csv")
img_path=os.path.join(dir_of_interest,"images","p.jpg")
img=image.imread(img_path)
st.image(img)
df=pd.read_csv(data_path)
df=df.drop(["Unnamed: 0"],axis=1)
local_authority=st.selectbox("select local_authority",df["local_authority"].unique())
button=st.button("search")
if button:
      

    n= df.loc[(df["local_authority"]==local_authority)]
    st.dataframe(n)
    st.map(n)

