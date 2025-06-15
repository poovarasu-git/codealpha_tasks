
import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import tempfile

model = load_model("model/handwritten_char_model.h5")

def predict_character(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (28, 28))
    img = img.reshape(1, 28, 28, 1) / 255.0
    pred = model.predict(img)
    return chr(np.argmax(pred) + ord('A'))

st.title("Handwritten Character Recognition")
uploaded_file = st.file_uploader("Upload a handwritten character image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=150)
    label = predict_character(image)
    st.success(f"Predicted Character: {label}")
