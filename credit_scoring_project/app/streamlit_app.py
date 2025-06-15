
import streamlit as st
import pandas as pd
import joblib
import pickle

# Load model and transformers
model = joblib.load("model/credit_model.pkl")
scaler = joblib.load("model/scaler.pkl")
with open("model/label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

st.title("🏦 Credit Scoring Prediction App")

uploaded_file = st.file_uploader("Upload customer data (CSV)", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    for col in data.columns:
        if col in label_encoders:
            data[col] = label_encoders[col].transform(data[col])

    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)
    prob = model.predict_proba(scaled_data)[:, 1]

    result = pd.DataFrame({
        "Prediction": prediction,
        "Default Probability": prob
    })

    st.write("### Prediction Results")
    st.write(result)
