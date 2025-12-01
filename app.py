import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os

# ---------------------------
# Get base directory
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for model and data
model_path = os.path.join(BASE_DIR, "model.pkl")
data_path = os.path.join(BASE_DIR, "data.pkl")

# ---------------------------
# Load model and data safely
# ---------------------------
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ model.pkl not found in the project folder!")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model.pkl: {e}")
    st.stop()

try:
    with open(data_path, "rb") as f:
        data = pickle.load(f)
except FileNotFoundError:
    st.error("❌ data.pkl not found in the project folder!")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading data.pkl: {e}")
    st.stop()

# ---------------------------
# App title
# ---------------------------
st.title("🌫️ Delhi AQI Prediction")
st.write("Predict Air Quality Index (AQI) using pollutants and date information.")

# ---------------------------
# Date and categorical inputs
# ---------------------------
st.subheader("📅 Date & Day Inputs")

# Select Date
date = st.selectbox("Select Date", sorted(data['Date'].unique()))
month = st.selectbox("Select Month", sorted(data['Month'].unique()))
year = st.selectbox("Select Year", sorted(data['Year'].unique()))

# Encode Days
days_mapping = {day: i for i, day in enumerate(sorted(data['Days'].unique()))}
day_name = st.selectbox("Day of the Week", sorted(data['Days'].unique()))
day = days_mapping[day_name]

# ---------------------------
# Sidebar sliders for pollutants
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
    # Feature order must match training
    input_values = np.array([[date, month, year, day, PM2_5, PM_10, NO_2, CO, Ozone]])
    
    try:
        prediction = float(model.predict(input_values)[0])
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
        st.stop()
    
    st.success(f"🌟 Predicted AQI: {prediction:.2f}")
    
    # AQI category
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
