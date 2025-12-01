import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os  # <-- For path handling

# ---------------------------
# Get current file directory
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------
# Load model and data
# ---------------------------
model_path = os.path.join(BASE_DIR, 'model.pkl')
data_path = os.path.join(BASE_DIR, 'data.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(data_path, 'rb') as f:
    data = pickle.load(f)

# ---------------------------
# App Title
# ---------------------------
st.title("🌫️ Air Quality Index (AQI) Prediction – Delhi")
st.write("Predict AQI using pollutant levels and date information.")

# ---------------------------
# Categorical Inputs
# ---------------------------
st.subheader("📅 Date & Day Inputs")

date = st.selectbox("Select Date", sorted(data['Date'].unique()))
month = st.selectbox("Select Month", sorted(data['Month'].unique()))
year = st.selectbox("Select Year", sorted(data['Year'].unique()))

# Encode Days if needed
days_mapping = {day: i for i, day in enumerate(sorted(data['Days'].unique()))}
day_name = st.selectbox("Day of Week", sorted(data['Days'].unique()))
day = days_mapping[day_name]  # numeric encoding

# ---------------------------
# Sidebar Sliders for Pollutants
# ---------------------------
st.sidebar.header("🌫️ Pollutant Levels")

PM2_5 = st.sidebar.slider("PM2.5", 0, 1000, 80)
PM_10 = st.sidebar.slider("PM10", 0, 1000, 200)
NO_2 = st.sidebar.slider("NO₂", 0, 450, 40)
CO = st.sidebar.slider("CO (mg/m³)", 0.0, 5.0, 1.0)
Ozone = st.sidebar.slider("Ozone", 0, 120, 40)

# ---------------------------
# Prediction
# ---------------------------
if st.button("Predict AQI"):
    # Ensure input order matches training features
    input_values = np.array([[date, month, year, day, PM2_5, PM_10, NO_2, CO, Ozone]])
    
    prediction = float(model.predict(input_values)[0])
    
    st.success(f"🌟 Predicted AQI: {prediction:.2f}")
    
    # AQI Category & Color
    if prediction <= 50:
        level = "Good 😊"
        color = "green"
    elif prediction <= 100:
        level = "Satisfactory 🙂"
        color = "yellow"
    elif prediction <= 200:
        level = "Moderate 😐"
        color = "orange"
    elif prediction <= 300:
        level = "Poor 😟"
        color = "red"
    else:
        level = "Severe 😷"
        color = "darkred"
    
    st.markdown(
        f"<div style='padding:10px;border-radius:8px;background-color:{color};color:white;'>"
        f"<h4>AQI Category: {level}</h4></div>",
        unsafe_allow_html=True
    )
