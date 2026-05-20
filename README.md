# 🌱 Crop Recommendation System (Streamlit + ML)

A simple machine learning web application that recommends the best crop to plant based on soil and environmental conditions. Built using **Streamlit** and a trained **Decision Tree Classifier (dtc.pkl)**.

---

## 🚀 Features

- 🌾 Predicts the most suitable crop based on input conditions  
- 📊 Uses trained ML model (Decision Tree Classifier)  
- 🧪 Takes soil nutrients and climate data as input:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH level
  - Rainfall
- ⚡ Real-time prediction using Streamlit UI  
- 🖥️ Simple and interactive web interface  

---

## 🧠 How It Works

1. User enters soil and environmental parameters  
2. Data is passed into a trained ML model  
3. Model predicts the most suitable crop  
4. Result is displayed instantly on the UI  

---

## 📂 Project Structure
<img width="1222" height="457" alt="image" src="https://github.com/user-attachments/assets/126beb42-4887-4739-a345-860201b2b4fc" />


---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/kanjifly.git
cd kanjifly
pip install -r requirements.txt
streamlit run app.py
http://localhost:8501

| Feature     | Description              | Range |
| ----------- | ------------------------ | ----- |
| N           | Nitrogen content in soil | 0–100 |
| P           | Phosphorus content       | 0–100 |
| K           | Potassium content        | 0–100 |
| Temperature | Air temperature (°C)     | 0–100 |
| Humidity    | Relative humidity (%)    | 0–100 |
| pH          | Soil acidity/alkalinity  | 0–14  |
| Rainfall    | Rainfall (mm)            | 0–500 |


Recommended Crop: Rice 🌾

👨‍💻 Author

Ibrahim Mustapha
AI / Computer Vision & Machine Learning Enthusiast 
