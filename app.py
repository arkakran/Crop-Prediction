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
st.title("Crop Prediction App")

# Input fields
st.header("Enter the Features:")
feature1 = st.number_input("Enter Feature 1 (e.g., Temperature):", value=0.0)
feature2 = st.number_input("Enter Feature 2 (e.g., Humidity):", value=0.0)

# Button for prediction
if st.button("Predict"):
    # Prepare input for the model
    features = np.array([[feature1, feature2]])
    
    # Get prediction
    prediction = model.predict(features)
    
    # Display prediction
    st.success(f"The Predicted Crop is: {prediction[0]}")

