

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


# import streamlit as st
# import numpy as np
# import pickle

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# # Streamlit App
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

# import streamlit as st
# import numpy as np
# import pickle

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# # Streamlit App with custom background from GitHub
# st.markdown(
#     """
#     <style>
#     body {
#         background-image: url('https://www.pexels.com/photo/top-view-of-green-field-1595104/');
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }
#     .stApp {
#         background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent background for readability */
#         padding: 10px;
#         border-radius: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

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






# import streamlit as st
# import numpy as np
# import pickle

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# # Streamlit App with custom background from Pexels
# st.markdown(
#     """
#     <style>
#     body {
#         background-image: url('https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg');  /* Direct image URL */
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }
#     .stApp {
#         background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent background for readability */
#         padding: 10px;
#         border-radius: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

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













# import streamlit as st

# # Inject CSS for background image
# background_image_url = "https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg"  

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

# # Render the background CSS
# st.markdown(page_bg, unsafe_allow_html=True)

# # Add some test content
# st.title("Test Background Image")
# st.write("If you can see the image in the background, it's working!")





import streamlit as st
import numpy as np
import pickle

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
st.subheader("Enter the required features to predict the best crop:")

# Input fields with range shown as placeholders
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
st.caption("Ensure the inputs are accurate to get the best prediction.")






