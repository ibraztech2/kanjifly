
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os


def run_check(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall):
    root = "C:\\Users\\State_Space_Lab\\3mtt folder\\machine learning\\kanjifly"
    dtc = "dtc.pkl"
    model_path = os.path.join(root, dtc)
    model = joblib.load(model_path)
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

#### Streamlit App
import streamlit as st

# Title
st.title("Crop Recommendation")
st.header("Get to Know What to Crop to Maximize Resources")
st.markdown("### Enter the details below to get the best crop recommendation based on your input.")

# Inputs
with st.form(key='input_form'):
    nitrogen = st.number_input("Nitrogen Level (0-100)",min_value=0.0, max_value=100.0, step=0.1)
    potassium = st.number_input("Potassium Level (0-100)",min_value=0.0, max_value=100.0, step=0.1)
    phosphorous = st.number_input("Phosphorous Level (0-100)", min_value=0.0, max_value=100.0, step=0.1)
    temperature = st.number_input("Ambient Temperature (°C)", min_value=0.0, max_value=100.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    rainfall = st.number_input("Rainfall Rate (mm)", min_value=0.0, max_value=100.0, step=0.1)
    ph = st.slider("PH Level (0-14)", min_value=0.0, max_value=14.0, step=0.1)
    
    # Submit button
    submit_button = st.form_submit_button(label='Predict')

# Prediction logic
if submit_button:
    if nitrogen and potassium and phosphorous and temperature and humidity and rainfall and ph:
        with st.spinner("Processing... Please wait."):
            # Assuming `run_check()` is the function that provides crop recommendation based on input
            predictions = run_check(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall)
            st.success(f"I recommend that you plant **{predictions}** based on your input.")
    else:
        st.error("Please fill all the input fields to get a recommendation.")
