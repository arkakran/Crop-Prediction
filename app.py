# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# # Create flask app
# flask_app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))

# @flask_app.route("/")
# def Home():
#     return render_template("index.html")

# @flask_app.route("/predict", methods = ["POST"])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template("index.html", prediction_text = "The Predicted Crop is {}".format(prediction))

# if __name__ == "__main__":
#     flask_app.run(debug=True)

import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit App
st.title("Crop Prediction Model")
st.subheader("Enter the required features to predict the best crop:")

# Input fields
nitrogen = st.number_input("Nitrogen Content (N):", min_value=0.0, step=0.1)
phosphorus = st.number_input("Phosphorus Content (P):", min_value=0.0, step=0.1)
potassium = st.number_input("Potassium Content (K):", min_value=0.0, step=0.1)
temperature = st.number_input("Temperature (°C):", min_value=-50.0, max_value=60.0, step=0.1)
humidity = st.number_input("Humidity (%):", min_value=0.0, max_value=100.0, step=0.1)
ph = st.number_input("Soil pH Level:", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm):", min_value=0.0, step=0.1)

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
