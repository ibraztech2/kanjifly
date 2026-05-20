# Kanjifly

A Streamlit-based crop recommendation app that predicts the best crop to plant from soil and weather inputs using a trained machine learning model (`dtc.pkl`).

## Features

- Simple web UI built with Streamlit
- Accepts key agronomic/environmental inputs:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall
- Returns a recommended crop label from the trained model

## Project Structure

- `app.py` – main Streamlit app and prediction logic
- `dtc.pkl` – serialized trained model
- `crop_dataset.csv` – dataset used in the project
- `ml_test.ipynb` – notebook for model experimentation
- `requirements.txt` – Python dependencies

## Requirements

- Python 3.9+ recommended

Install dependencies:

```bash
pip install -r requirements.txt
pip install streamlit pandas
```

## Run the App

```bash
# Navigate to your local project directory
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## How It Works

1. User enters soil and weather values in the form.
2. The app loads `dtc.pkl` once (cached).
3. Inputs are assembled into a DataFrame with expected model columns.
4. The model predicts a crop, and the result is displayed in the UI.

## Notes

- Ensure `dtc.pkl` is present in the project root before running.
- Input ranges in the UI are constrained for safer entry, but realistic values will produce better recommendations.
