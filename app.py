import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("house_price_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(page_title="House Price Prediction", layout="wide")

# =====================
# TITLE
# =====================
st.title("🏠 House Price Prediction App")
st.write(
    """
    A machine learning application to predict house prices  
    based on property characteristics.
    """
)

# =====================
# SIDEBAR INPUT
# =====================
st.sidebar.header("🏡 House Features")

input_data = {}

# ---- Basic Property Info
st.sidebar.subheader("Basic Information")
input_data["OverallQual"] = st.sidebar.slider("Overall Quality (1–10)", 1, 10, 5)
input_data["OverallCond"] = st.sidebar.slider("Overall Condition (1–10)", 1, 10, 5)
input_data["YearBuilt"] = st.sidebar.number_input("Year Built", 1800, 2025, 2000)
input_data["YearRemodAdd"] = st.sidebar.number_input("Year Remodeled", 1800, 2025, 2000)

# ---- Area Info
st.sidebar.subheader("Area (sqft)")
input_data["GrLivArea"] = st.sidebar.number_input("Living Area", 300, 10000, 1500)
input_data["LotArea"] = st.sidebar.number_input("Lot Area", 500, 200000, 8000)
input_data["TotalBsmtSF"] = st.sidebar.number_input("Basement Area", 0, 5000, 800)

# ---- Rooms
st.sidebar.subheader("Rooms")
input_data["BedroomAbvGr"] = st.sidebar.slider("Bedrooms", 0, 10, 3)
input_data["FullBath"] = st.sidebar.slider("Full Bathrooms", 0, 5, 2)
input_data["HalfBath"] = st.sidebar.slider("Half Bathrooms", 0, 3, 1)
input_data["TotRmsAbvGrd"] = st.sidebar.slider("Total Rooms", 2, 15, 6)

# ---- Garage
st.sidebar.subheader("Garage")
input_data["GarageCars"] = st.sidebar.slider("Garage Capacity (Cars)", 0, 5, 2)
input_data["GarageArea"] = st.sidebar.number_input("Garage Area", 0, 2000, 400)

# ---- Fill missing features with 0
for col in features:
    if col not in input_data:
        input_data[col] = 0

# =====================
# PREDICTION
# =====================
if st.button("🔮 Predict House Price"):
    input_df = pd.DataFrame([input_data])[features]
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated House Price: **${prediction:,.2f}**")

    st.caption("⚠️ This prediction is based on historical Ames Housing data.")
