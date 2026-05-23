

# 🌱 Smart Agriculture AI System

An AI-powered agricultural assistant that combines:

- 🌾 Crop Recommendation System  
- 🩺 Plant Disease Diagnosis System  

This project helps farmers and agricultural researchers make intelligent farming decisions using Machine Learning and Computer Vision.

---

# 🚀 Features

## 🌾 Crop Recommendation
Predicts the most suitable crop based on:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

---

## 🩺 Plant Disease Diagnosis
Detects plant diseases from uploaded leaf images using a YOLOv8 classification model.

Supported classes:

- Pepper Bell Bacterial Spot  
- Pepper Bell Healthy  
- Potato Early Blight  
- Potato Late Blight  
- Potato Healthy  
- Tomato Bacterial Spot  
- Tomato Early Blight  
- Tomato Healthy  

---

# 🧠 Technologies Used

- Python  
- Streamlit  
- YOLOv8  
- PyTorch  
- Scikit-learn  
- Pandas  
- NumPy  
- Pillow  

---

# 📁 Project Structure

project/
│
├── app.py
├── dtc.pkl
├── requirements.txt
├── runs/
└── assets/


---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/ibraztech2/kanjifly.git
cd kanjifly
```

2. Install Dependencies

pip install -r requirements.txt

## ▶️ Run the Application
``` bash
streamlit run app.py
```


### 🌾 Crop Recommendation Workflow
User enters soil and weather parameters ML model processes input System predicts best crop 🩺 Disease Diagnosis Workflow User uploads plant leaf image YOLOv8 model analyzes image Disease class is predicted Confidence score is displayed 

👨‍💻 Author: `Ibrahim Mustapha`

Interests: Computer Vision Deep Learning Smart Agriculture Embedded Systems AI for Social Good