
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
import googlemaps
import os
import requests

# Set your Google API key (environment variable recommended)
api_key = os.getenv("GOOGLE_API_KEY")  # Fetch API key securely from the environment

if not api_key:
    st.error("Google Maps API key not found! Please set your API key.")
    st.stop()  # Stop execution if the API key is missing

# Function to get coordinates using the Google Maps API
def get_location_coordinates(api_key, country, state, city, area):
    gmaps = googlemaps.Client(key=api_key)
    location = f"{area}, {city}, {state}, {country}"
    try:
        geocode_result = gmaps.geocode(location)
        if geocode_result:
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lon = geocode_result[0]["geometry"]["location"]["lng"]
            return lat, lon
        else:
            st.error("Could not fetch coordinates. Please check the location details.")
            return None, None
    except Exception as e:
        st.error(f"Error fetching coordinates: {str(e)}")
        return None, None

# Function to fetch weather data (Temperature, Humidity) based on coordinates
def get_weather_data(lat, lon):
    weather_api_key = "YOUR_OPENWEATHER_API_KEY"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        if response.status_code == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            return temperature, humidity
        else:
            st.error("Could not fetch weather data. Please try again later.")
            return None, None
    except Exception as e:
        st.error(f"Error fetching weather data: {str(e)}")
        return None, None

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit layout and UI components
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

st.title("Crop Prediction Model")
st.subheader("Enter location and other features to predict the best crop:")

# Location input fields for country, state, city, and area
country = st.text_input("Enter Country:")
state = st.text_input("Enter State:")
city = st.text_input("Enter City:")
area = st.text_input("Enter Area/Village Name:")

# Inputs for other crop features (N, P, K, pH, etc.)
nitrogen = st.text_input("Nitrogen Content (N):", placeholder="Enter a value between 0-300")
phosphorus = st.text_input("Phosphorus Content (P):", placeholder="Enter a value between 0-150")
potassium = st.text_input("Potassium Content (K):", placeholder="Enter a value between 0-800")
temperature = st.text_input("Temperature (°C):", placeholder="Enter a value between -5 to 50")
humidity = st.text_input("Humidity (%):", placeholder="Enter a value between 20-100")
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

# Button to get weather data and predict crop
if st.button("Fetch Weather and Predict Crop"):
    # Fetch the coordinates based on location
    lat, lon = get_location_coordinates(api_key, country, state, city, area)

    if lat is not None and lon is not None:
        # Fetch weather data (Temperature, Humidity)
        temp, hum = get_weather_data(lat, lon)
        if temp is not None and hum is not None:
            # Display fetched weather data
            st.write(f"Temperature: {temp}°C")
            st.write(f"Humidity: {hum}%")

            # If weather data is successfully fetched, use it for prediction
            temperature = temp
            humidity = hum

            # Check if inputs are within valid ranges
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
                # Prepare input features for the prediction
                features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

                # Get prediction from the model
                prediction = model.predict(features)

                # Display prediction
                st.success(f"The predicted crop is: {prediction[0]}")
        else:
            st.error("Could not fetch weather data.")
    else:
        st.error("Invalid location. Please check the inputs.")

# Note for user
st.caption("Ensure the inputs are accurate to get the best prediction.")

