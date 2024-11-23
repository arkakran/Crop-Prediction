
# import streamlit as st
# import numpy as np
# import pickle

# # Add background image
# background_image_url = "https://images.pexels.com/photos/91115/pexels-photo-91115.jpeg"  
# page_bg = f"""
# <style>
# .stApp {{
#     background-image: url("{background_image_url}");
#     background-size: cover;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }}
# </style>
# """
# st.markdown(page_bg, unsafe_allow_html=True)

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# st.title("Crop Prediction Model")
# st.subheader("Enter the required features to predict the best crop:")

# # Input fields with range shown as placeholders
# nitrogen = st.text_input("Nitrogen Content (N):", placeholder="Enter a value between 0-300")
# phosphorus = st.text_input("Phosphorus Content (P):", placeholder="Enter a value between 0-150")
# potassium = st.text_input("Potassium Content (K):", placeholder="Enter a value between 0-800")
# temperature = st.text_input("Temperature (°C):", placeholder="Enter a value between -5 to 50")
# humidity = st.text_input("Humidity (%):", placeholder="Enter a value between 20-100")
# ph = st.text_input("Soil pH Level:", placeholder="Enter a value between 4.0-9.0")
# rainfall = st.text_input("Rainfall (mm):", placeholder="Enter a value between 0-3000")

# # Convert inputs to float (with validation)
# try:
#     nitrogen = float(nitrogen) if nitrogen else 0
#     phosphorus = float(phosphorus) if phosphorus else 0
#     potassium = float(potassium) if potassium else 0
#     temperature = float(temperature) if temperature else 0
#     humidity = float(humidity) if humidity else 0
#     ph = float(ph) if ph else 0
#     rainfall = float(rainfall) if rainfall else 0
# except ValueError:
#     st.error("Please enter valid numeric values in all fields!")

# # Button for prediction
# if st.button("Predict"):
#     # Check if inputs are within range
#     if not (0 <= nitrogen <= 300):
#         st.error("Nitrogen value should be between 0 and 300.")
#     elif not (0 <= phosphorus <= 150):
#         st.error("Phosphorus value should be between 0 and 150.")
#     elif not (0 <= potassium <= 800):
#         st.error("Potassium value should be between 0 and 800.")
#     elif not (-5 <= temperature <= 50):
#         st.error("Temperature should be between -5 and 50°C.")
#     elif not (20 <= humidity <= 100):
#         st.error("Humidity should be between 20 and 100%.")
#     elif not (4.0 <= ph <= 9.0):
#         st.error("Soil pH Level should be between 4.0 and 9.0.")
#     elif not (0 <= rainfall <= 3000):
#         st.error("Rainfall should be between 0 and 3000 mm.")
#     else:
#         # Prepare input features
#         features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        
#         # Get prediction
#         prediction = model.predict(features)
        
#         # Display prediction
#         st.success(f"The predicted crop is: {prediction[0]}")

# # Note for user
# st.caption("Ensure the inputs are accurate to get the best prediction.")










import streamlit as st
import numpy as np
import pickle
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import json

# OpenWeatherMap API configuration
OPENWEATHER_API_KEY = "API KEY"  # Replace with your API key

def get_location_coordinates(location_name):
    """Get coordinates for a given location name using Nominatim"""
    try:
        geolocator = Nominatim(user_agent="crop_prediction_app")
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
        return None
    except GeocoderTimedOut:
        return None

def get_weather_data(lat, lon):
    """Fetch weather data from OpenWeatherMap API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity']
            }
        return None
    except Exception as e:
        st.error(f"Error fetching weather data: {str(e)}")
        return None

# Add background image
background_image_url = "https://images.pexels.com/photos/91115/pexels-photo-91115.jpeg"  
page_bg = f"""
<style>
.stApp {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Crop Prediction Model")
st.subheader("Enter location or manual values to predict the best crop:")

# Location input
location_col, weather_data_col = st.columns(2)

with location_col:
    location = st.text_input("Enter Location (City, Country):", placeholder="e.g., London, UK")
    if st.button("Get Weather Data"):
        if location:
            coordinates = get_location_coordinates(location)
            if coordinates:
                weather_data = get_weather_data(coordinates[0], coordinates[1])
                if weather_data:
                    st.session_state['temperature'] = weather_data['temperature']
                    st.session_state['humidity'] = weather_data['humidity']
                    st.success("Weather data fetched successfully!")
                else:
                    st.error("Could not fetch weather data. Please enter values manually.")
            else:
                st.error("Location not found. Please check the location name.")

# Initialize session state for temperature and humidity if not exists
if 'temperature' not in st.session_state:
    st.session_state['temperature'] = ''
if 'humidity' not in st.session_state:
    st.session_state['humidity'] = ''

# Input fields
nitrogen = st.text_input("Nitrogen Content (N):", placeholder="Enter a value between 0-300")
phosphorus = st.text_input("Phosphorus Content (P):", placeholder="Enter a value between 0-150")
potassium = st.text_input("Potassium Content (K):", placeholder="Enter a value between 0-800")
temperature = st.text_input("Temperature (°C):", 
                          value=st.session_state['temperature'],
                          placeholder="Enter a value between -5 to 50")
humidity = st.text_input("Humidity (%):", 
                        value=st.session_state['humidity'],
                        placeholder="Enter a value between 20-100")
ph = st.text_input("Soil pH Level:", placeholder="Enter a value between 4.0-9.0")
rainfall = st.text_input("Rainfall (mm):", placeholder="Enter a value between 0-3000")

# Convert inputs to float (with validation)
try:
    nitrogen = float(nitrogen) if nitrogen else 0
    phosphorus = float(phosphorus) if phosphorus else 0
    potassium = float(potassium) if potassium else 0
    temperature = float(temperature) if temperature else 0
    humidity = float(humidity) if humidity else 0
    ph = float(ph) if ph else 0
    rainfall = float(rainfall) if rainfall else 0
except ValueError:
    st.error("Please enter valid numeric values in all fields!")

# Button for prediction
if st.button("Predict"):
    # Check if inputs are within range
    if not (0 <= nitrogen <= 300):
        st.error("Nitrogen value should be between 0 and 300.")
    elif not (0 <= phosphorus <= 150):
        st.error("Phosphorus value should be between 0 and 150.")
    elif not (0 <= potassium <= 800):
        st.error("Potassium value should be between 0 and 800.")
    elif not (-5 <= temperature <= 50):
        st.error("Temperature should be between -5 and 50°C.")
    elif not (20 <= humidity <= 100):
        st.error("Humidity should be between 20 and 100%.")
    elif not (4.0 <= ph <= 9.0):
        st.error("Soil pH Level should be between 4.0 and 9.0.")
    elif not (0 <= rainfall <= 3000):
        st.error("Rainfall should be between 0 and 3000 mm.")
    else:
        # Prepare input features
        features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        
        # Get prediction
        prediction = model.predict(features)
        
        # Display prediction
        st.success(f"The predicted crop is: {prediction[0]}")

# Note for user
st.caption("You can either enter location to auto-fill weather data or input values manually.")

