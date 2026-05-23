# Smart Agriculture AI Web App


import streamlit as st
import numpy as np
import pandas as pd
import joblib
import torch
import torch.nn as nn
from ultralytics import YOLO
from PIL import Image

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Smart Agriculture AI",
    page_icon="🌱",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown(
    """
    <style>
    .main {
        background-color: #f5fff5;
    }

    .stButton>button {
        background-color: #2e8b57;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }

    .stButton>button:hover {
        background-color: #246b45;
        color: white;
    }

    .title {
        text-align: center;
        color: #2e8b57;
        font-size: 45px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #444;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# TITLE
# =====================================================
st.markdown('<p class="title">🌱 Smart Agriculture AI System</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Crop Recommendation + Plant Disease Diagnosis</p>',
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Select AI Service",
    [
        "🌾 Crop Recommendation",
        "🩺 Plant Disease Diagnosis"
    ]
)

# =====================================================
# LOAD CROP RECOMMENDATION MODEL
# =====================================================
@st.cache_resource

def load_crop_model():
    return joblib.load("dtc.pkl")

# =====================================================
# CROP PREDICTION FUNCTION
# =====================================================
def run_crop_recommendation(
    nitrogen,
    phosphorous,
    potassium,
    temperature,
    humidity,
    ph,
    rainfall
):

    model = load_crop_model()

    columns = [
        'N',
        'P',
        'K',
        'temperature',
        'humidity',
        'ph',
        'rainfall'
    ]

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

    prediction = model.predict(data)

    return prediction[0]

# =====================================================
# CUSTOM YOLO HEAD
# =====================================================
class PlantHead(nn.Module):
    def __init__(self):
        super(PlantHead, self).__init__()
        self.fc = nn.Linear(1024, 8)

    def forward(self, x):
        x = self.fc(x)
        return x

# =====================================================
# LOAD PLANT DISEASE MODEL
# =====================================================
@st.cache_resource

def load_disease_model():

    model_path = "best.pt"

    model = YOLO(model_path)

    return model

# =====================================================
# DISEASE CLASS NAMES
# =====================================================
class_names = ['Pepper__bell___healthy', 'Tomato_Leaf_Mold', 'Tomato_Early_blight', 'Tomato__Tomato_mosaic_virus', 'Tomato_Late_blight', 'Tomato_healthy', 'Potato___Late_blight', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Potato___healthy', 'Pepper__bell___Bacterial_spot', 'Potato___Early_blight', 'Tomato_Septoria_leaf_spot', 'Tomato_Bacterial_spot']

# =====================================================
# CROP RECOMMENDATION PAGE
# =====================================================
if option == "🌾 Crop Recommendation":

    st.header("🌾 Crop Recommendation System")
    st.write("Enter environmental and soil parameters to get the best crop recommendation.")

    with st.form(key='crop_form'):

        col1, col2 = st.columns(2)

        with col1:
            nitrogen = st.number_input(
                "Nitrogen Level (0-100)",
                0.0,
                100.0,
                step=0.1
            )

            phosphorous = st.number_input(
                "Phosphorous Level (0-100)",
                0.0,
                100.0,
                step=0.1
            )

            potassium = st.number_input(
                "Potassium Level (0-100)",
                0.0,
                100.0,
                step=0.1
            )

            temperature = st.number_input(
                "Temperature (°C)",
                0.0,
                100.0,
                step=0.1
            )

        with col2:
            humidity = st.number_input(
                "Humidity (%)",
                0.0,
                100.0,
                step=0.1
            )

            rainfall = st.number_input(
                "Rainfall (mm)",
                0.0,
                500.0,
                step=0.1
            )

            ph = st.slider(
                "PH Level",
                0.0,
                14.0,
                step=0.01
            )

        submit_button = st.form_submit_button("Predict Crop")

    if submit_button:

        with st.spinner("Analyzing soil and climate conditions..."):

            prediction = run_crop_recommendation(
                nitrogen,
                phosphorous,
                potassium,
                temperature,
                humidity,
                ph,
                rainfall
            )

        st.success(f"🌱 Recommended Crop: {prediction}")

# =====================================================
# PLANT DISEASE DIAGNOSIS PAGE
# =====================================================
if option == "🩺 Plant Disease Diagnosis":

    st.header("🩺 Plant Disease Diagnosis")
    st.write("Upload a plant leaf image for disease detection.")

    uploaded_file = st.file_uploader(
        "Upload Leaf Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        image = image.resize(size=(256, 256))
        

        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Diagnose Plant"):

            with st.spinner("Analyzing plant image..."):

                model = load_disease_model()

                results = model.predict(image)

                probs = results[0].probs

                predicted_class = int(probs.top1)

                confidence = float(probs.top1conf) * 100

                disease_name = class_names[predicted_class]

            st.success(f"Prediction: {disease_name}")
            st.info(f"Confidence: {confidence:.2f}%")

# =====================================================
# FOOTER
# =====================================================
st.divider()

st.markdown(
    """
    ### 🌍 Features

    - Crop Recommendation Using Soil & Weather Data
    - Plant Disease Diagnosis Using Computer Vision
    - YOLOv8 Classification Model
    - Interactive Streamlit Dashboard
    """
)

