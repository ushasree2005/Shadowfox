# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model (must be in same folder)
model = joblib.load("model.pkl")

st.set_page_config(page_title="Boston House Price Prediction", page_icon="🏠", layout="centered")
st.title("🏠 Boston House Price Prediction")
st.write("Enter house details below to predict the price (in $1000s).")

CRIM = st.number_input("Per capita crime rate (CRIM)", 0.0, 100.0, 0.1)
ZN = st.number_input("Residential land zoned (ZN)", 0.0, 100.0, 0.0)
INDUS = st.number_input("Non-retail business acres (INDUS)", 0.0, 50.0, 10.0)
CHAS = st.selectbox("Charles River bounds (CHAS)", [0, 1])
NOX = st.number_input("Nitric oxide concentration (NOX)", 0.0, 1.0, 0.5)
RM = st.number_input("Average rooms per dwelling (RM)", 1.0, 10.0, 6.0)
AGE = st.number_input("Proportion of old units (AGE)", 0.0, 100.0, 50.0)
DIS = st.number_input("Weighted distances to employment centers (DIS)", 0.0, 20.0, 4.0)
RAD = st.number_input("Access to highways (RAD)", 1, 24, 5)
TAX = st.number_input("Property tax rate (TAX)", 100, 1000, 300)
PTRATIO = st.number_input("Pupil-teacher ratio (PTRATIO)", 10.0, 30.0, 18.0)
B = st.number_input("1000(Bk - 0.63)^2 (B)", 0.0, 500.0, 350.0)
LSTAT = st.number_input("Lower status % (LSTAT)", 0.0, 100.0, 12.0)

if st.button("🔮 Predict House Price"):
    input_data = pd.DataFrame({
        "CRIM": [CRIM], "ZN": [ZN], "INDUS": [INDUS], "CHAS": [CHAS],
        "NOX": [NOX], "RM": [RM], "AGE": [AGE], "DIS": [DIS],
        "RAD": [RAD], "TAX": [TAX], "PTRATIO": [PTRATIO], "B": [B], "LSTAT": [LSTAT]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Predicted House Price: **${prediction * 1000:,.2f} USD**")

st.caption("Developed by Popperite 🧠 | Powered by Streamlit & Scikit-learn")
