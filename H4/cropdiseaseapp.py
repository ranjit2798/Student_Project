import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import json

# Load the model and class indices
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("plant_disease.keras")
    return model

@st.cache_data
def load_class_indices():
    with open("class_indices.json", "r") as file:
        class_indices = json.load(file)
    return {v: k for k, v in class_indices.items()}

# Load resources
model = load_model()
class_indices = load_class_indices()

def predict_disease(image):
    # Preprocess the image
    img = img_to_array(image)
    img = tf.image.resize(img, (224, 224)) / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    return class_indices[predicted_class], confidence

# Streamlit app interface
st.title("Crop Disease Prediction")
st.write("Upload an image of a plant leaf to detect potential diseases.")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display the uploaded image
    image = load_img(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make a prediction
    with st.spinner("Analyzing the image..."):
        disease, confidence = predict_disease(image)

    # Display results
    st.success("Prediction complete!")
    st.write(f"### Predicted Disease: {disease}")
    st.write(f"### Confidence: {confidence * 100:.2f}%")
