import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageEnhance

st.set_page_config(page_title="Diabetes Testing",
                   page_icon=":🍾:",
                   layout="centered")

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

st.markdown("<h1 style='color: black;'>What is Diabetes?</h1>", unsafe_allow_html=True)
st.markdown('''
    <h4 style='color: black;'>
        Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood glucose.)
        <br><br>
        In 2014, 8.5% of adults aged 18 years and older had diabetes. In 2019, diabetes was the direct cause of 1.5 million deaths and 48% of all deaths due to diabetes occurred before the age of 70 years.
        <br><br>
        Between 2000 and 2019, there was a 3% increase in age-standardized mortality rates from diabetes. In lower-middle-income countries, the mortality rate due to diabetes increased 13%.
    </h4>
''', unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Symptoms</h1>", unsafe_allow_html=True)
st.markdown('''
    <h4 style='color: black;'>
        Symptoms of diabetes may occur suddenly. In type 2 diabetes, the symptoms can be mild and may take many years to be noticed.
        <br><br>
        Symptoms of diabetes include:
        <br><br>
        - Feeling very thirsty
        - Needing to urinate more often than usual
        - Blurred vision
        - Feeling tired
        - Losing weight unintentionally
        <br><br>
        Over time, diabetes can damage blood vessels in the heart, eyes, kidneys, and nerves.
        <br><br>
        People with diabetes have a higher risk of health problems including heart attack, stroke, and kidney failure.
        <br><br>
        Diabetes can cause permanent vision loss by damaging blood vessels in the eyes.
        <br><br>
        Many people with diabetes develop problems with their feet from nerve damage and poor blood flow. This can cause foot ulcers and may lead to amputation.
    </h4>
''', unsafe_allow_html=True)
st.markdown("<h1 style='color: black;'>Prevention</h1>", unsafe_allow_html=True)

st.markdown('''
    <h4 style='color: black;'>
        Lifestyle changes are the best way to prevent or delay the onset of type 2 diabetes.
        <br><br>
        To help prevent type 2 diabetes and its complications, people should:
        <br><br>
        - Reach and maintain a healthy body weight
        - Stay physically active with at least 30 minutes of moderate exercise each day
        - Eat a healthy diet and avoid sugar and saturated fat
        - Not smoke tobacco
    </h4>
''', unsafe_allow_html=True)
