

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

@st.cache_resource
def load_model():
    return joblib.load("dtc.pkl")

def run_check(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall):
    model = load_model()
    columns = [ 'N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall' ]
    data = np.array([[
        nitrogen,
        phosphorous,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ]])
    data = pd.DataFrame(data, columns=columns)
    predictions = model.predict(data)
    suggestions = predictions[0]
    return suggestions
import streamlit as st

# Title
st.title("Crop Recommendation")
st.header("Get to Know What Crop to Plant Based on Your Environment")
st.markdown("### Enter the details below to get the best crop recommendation.")

# Form
with st.form(key='input_form'):
    nitrogen = st.number_input("Nitrogen Level (0-100)", 0.0, 100.0, step=0.1)
    phosphorous = st.number_input("Phosphorous Level (0-100)", 0.0, 100.0, step=0.1)
    potassium = st.number_input("Potassium Level (0-100)", 0.0, 100.0, step=0.1)
    temperature = st.number_input("Temperature (°C)", 0.0, 100.0, step=0.1)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 100.0, step=0.1)
    ph = st.slider("PH Level", 0.0, 14.0, step=0.1)

    submit_button = st.form_submit_button("Predict")

# Prediction
if submit_button:
    with st.spinner("Running model..."):
        prediction = run_check(
            nitrogen,
            phosphorous,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

    st.success(f"🌱 Recommended Crop: **{prediction}**")
