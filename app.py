

# import streamlit as st
# import numpy as np
# import pickle

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# # Streamlit App
# st.title("Crop Prediction Model")
# st.subheader("Enter the required features to predict the best crop:")

# # Input fields
# nitrogen = st.number_input("Nitrogen Content (N):", min_value=0.0, max_value=300.0, step=0.1)
# phosphorus = st.number_input("Phosphorus Content (P):", min_value=0.0, max_value=150.0, step=0.1)
# potassium = st.number_input("Potassium Content (K):", min_value=0.0, max_value=800.0, step=0.1)
# temperature = st.number_input("Temperature (°C):", min_value=-5.0, max_value=50.0, step=0.1)
# humidity = st.number_input("Humidity (%):", min_value=20.0, max_value=100.0, step=0.1)
# ph = st.number_input("Soil pH Level:", min_value=4.0, max_value=9.0, step=0.1)
# rainfall = st.number_input("Rainfall (mm):", min_value=0.0, max_value=3000.0, step=0.1)

# # Button for prediction
# if st.button("Predict"):
#     # Prepare input features
#     features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
    
#     # Get prediction
#     prediction = model.predict(features)
    
#     # Display prediction
#     st.success(f"The predicted crop is: {prediction[0]}")

# # Note for user
# st.caption("Ensure the inputs are accurate to get the best prediction.")

import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit App
st.title("Crop Prediction Model")
st.subheader("Enter the required features to predict the best crop:")

# Input fields with min, max values, and range description
nitrogen = st.number_input(
    "Nitrogen Content (N):",
    min_value=0.0,
    max_value=300.0,
    step=0.1,
    help="Enter Nitrogen content in the range 0-300 kg/ha."
)
phosphorus = st.number_input(
    "Phosphorus Content (P):",
    min_value=0.0,
    max_value=150.0,
    step=0.1,
    help="Enter Phosphorus content in the range 0-150 kg/ha."
)
potassium = st.number_input(
    "Potassium Content (K):",
    min_value=0.0,
    max_value=800.0,
    step=0.1,
    help="Enter Potassium content in the range 0-800 kg/ha."
)
temperature = st.number_input(
    "Temperature (°C):",
    min_value=-5.0,
    max_value=50.0,
    step=0.1,
    help="Enter Temperature in the range -5 to 50°C."
)
humidity = st.number_input(
    "Humidity (%):",
    min_value=20.0,
    max_value=100.0,
    step=0.1,
    help="Enter Humidity in the range 20-100%."
)
ph = st.number_input(
    "Soil pH Level:",
    min_value=4.0,
    max_value=9.0,
    step=0.1,
    help="Enter Soil pH Level in the range 4.0-9.0."
)
rainfall = st.number_input(
    "Rainfall (mm):",
    min_value=0.0,
    max_value=3000.0,
    step=0.1,
    help="Enter Rainfall in the range 0-3000 mm."
)

# Button for prediction
if st.button("Predict"):
    # Prepare input features
    features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
    
    # Get prediction
    prediction = model.predict(features)
    
    # Display prediction
    st.success(f"The predicted crop is: {prediction[0]}")

# Note for user
st.caption("Ensure the inputs are accurate to get the best prediction.")
