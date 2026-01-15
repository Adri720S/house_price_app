import streamlit as st
import pandas as pd
import joblib

# Load model & feature list
model = joblib.load("house_price_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(page_title="House Price Prediction", layout="wide")
st.title("🏠 House Price Prediction App")

st.write("Masukkan fitur rumah di bawah ini untuk memprediksi harga")

# Input form
input_data = {}

cols = st.columns(3)
for i, feature in enumerate(features):
    with cols[i % 3]:
        input_data[feature] = st.number_input(
            label=feature,
            value=0.0
        )

# Predict
if st.button("Predict House Price"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated House Price: ${prediction:,.2f}")
