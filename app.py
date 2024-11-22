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
import pickle
import numpy as np

# Load your model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit interface
st.title("Crop Prediction App")

# Form for user input
with st.form("prediction_form"):
    feature1 = st.number_input("Enter Feature 1")
    feature2 = st.number_input("Enter Feature 2")
    submitted = st.form_submit_button("Predict")

    if submitted:
        # Assuming model expects a 2D array
        prediction = model.predict(np.array([[feature1, feature2]]))
        st.write(f"Prediction: {prediction[0]}")
