import streamlit as st
import os
import numpy as np
from pickle import load

st.set_page_config(page_title="Diabetes Testing",
                   layout="centered")

st.sidebar.title("Diabetes Testing App")
st.sidebar.markdown("Here you can enter you values and check wheater you have Diabetes or not")

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

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

MODEL_PATH = os.path.join(dir_of_interest, 'diabetes.pkl')
SCALAR_PATH = os.path.join(dir_of_interest, 'scalar.pkl')

model = load(open(MODEL_PATH, 'rb'))
sc = load(open(SCALAR_PATH, 'rb'))

# sc = load(open('scalar.pkl', 'rb'))
# model = load(open('diabites.pkl','rb'))


st.markdown("<h2 style='color: black;'>Diabetes Testing:</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    preg = st.text_input("Pregnancies", placeholder="Enter the value")

with col2:
    glucose = st.text_input("Glucose", placeholder="Enter the value")

col3, col4 = st.columns(2)
with col3:
    bp = st.text_input("BloodPressure", placeholder="Enter the value")
with col4:
    stk = st.text_input("SkinThickness", placeholder="Enter the value")

col5, col6 = st.columns(2)
with col5:
    insulin = st.text_input("Insulin", placeholder="Enter the value")
with col6:
    bmi = st.text_input("BMI", placeholder="Enter the value")

col7, col8 = st.columns(2)
with col7:
    dpf = st.text_input("DPF", placeholder="Enter the value")
with col8:
    age = st.text_input("Age", placeholder="Enter the value")

btn_click = st.button("Predict")

if btn_click == True:
    if preg and glucose and bp and stk and insulin and bmi and dpf and age:
        query_point = np.array(
            [int(preg), float(glucose), float(bp), float(stk), float(insulin), float(bmi), float(dpf),
             int(age)]).reshape(1, -1)
        query_point = sc.transform(query_point)
        pred = model.predict(query_point)

        if pred[0] == 1:
            st.markdown("<h2 style='color: red;'>You have diabetes.</h2>", unsafe_allow_html=True)
            st.markdown("<h1 style='color: black;'>Diagnosis and treatment</h1>", unsafe_allow_html=True)
            st.markdown('''
                <h4 style='color: black;'>
                    Early diagnosis can be accomplished through relatively inexpensive testing of blood glucose. People with type 1 diabetes need insulin injections for survival.
                    <br><br>
                    One of the most important ways to treat diabetes is to keep a healthy lifestyle.
                    <br><br>
                    Some people with type 2 diabetes will need to take medicines to help manage their blood sugar levels. These can include insulin injections or other medicines. Some examples include:
                    <br><br>
                    - Metformin,
                    - Sulfonylureas,
                    - Sodium-glucose co-transporters type 2 (SGLT-2) inhibitors.
                    Along with medicines to lower blood sugar, people with diabetes often need medications to lower their blood pressure and statins to reduce the risk of complications. 
                    <br><br>
                    Additional medical care may be needed to treat the effects of diabetes:
                    <br><br>
                    - foot care to treat ulcers
                    - screening and treatment for kidney disease
                    - eye exams to screen for retinopathy (which causes blindness). 
                </h4>    
            ''', unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color: green;'>You don't have diabetes.</h2>", unsafe_allow_html=True)

    else:
        st.error("Enter the values properly.")