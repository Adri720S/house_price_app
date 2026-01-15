import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(page_title="House Price Prediction", layout="wide")
st.title("🏠 House Price Prediction App")
