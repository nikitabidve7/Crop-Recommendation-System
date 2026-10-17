import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load("/Users/DELL/OneDrive/mtech/Research/implent/crop_model.pkl")

st.title("🌱 Smart Crop Recommendation System")
st.write("Enter the soil and environmental parameters to find the best crop to grow.")

# Create input sliders/number boxes for the user
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N ratio)", min_value=0.0, max_value=150.0, value=50.0)
    P = st.number_input("Phosphorus (P ratio)", min_value=0.0, max_value=150.0, value=50.0)
    K = st.number_input("Potassium (K ratio)", min_value=0.0, max_value=205.0, value=50.0)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)

with col2:
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)
    ph = st.number_input("Soil pH Value", min_value=0.0, max_value=14.0, value=6.5)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0)

# Prediction button
if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    
    st.success(f"The most suitable crop to grow is: **{prediction[0].upper()}**!")


