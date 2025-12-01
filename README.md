### Delhi AQI Prediction 🌫️

A Streamlit web app to predict Delhi’s Air Quality Index (AQI) using daily pollutant levels and date information.

![Project Logo](https://img.shields.io/badge/Streamlit-Deployed-green)
**Deployed Application:** [Visit the App](https://delhiaqidataset-wjvu3umcvt2llbfstnnnul.streamlit.app/)

---
### Features
- Predict AQI using PM2.5, PM10, NO₂, CO, Ozone
- Input date and day for prediction
- Displays AQI category with color labels
- Interactive sliders for pollutant inputs

---
### Installation
- git clone https://github.com/username/Delhi_AQI_Dataset.git
- cd Delhi_AQI_Dataset
- pip install -r requirements.txt

---
Usage
streamlit run app.py
Select Date, Month, Year, Day
Adjust pollutant sliders
Click Predict AQI

---
AQI Categories
AQI	Category
0-50	Good 😊
51-100	Satisfactory 🙂
101-200	Moderate 😐
201-300	Poor 😟
301+	Severe 😷

---
Requirements
Python 3.8+
streamlit, pandas, numpy, tensorflow, scikit-learn
