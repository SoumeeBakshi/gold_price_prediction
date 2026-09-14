import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

st.title("Gold Price (GLD) Prediction")
st.write("Enter the market values below to predict the gold price.")

# Input fields - order matches training data: SPX, USO, SLV, EUR/USD
spx = st.number_input("SPX (S&P 500 Index)", value=1400.0)
uso = st.number_input("USO (Oil ETF)", value=35.0)
slv = st.number_input("SLV (Silver ETF)", value=15.0)
eur_usd = st.number_input("EUR/USD", value=1.10)

if st.button("Predict GLD Price"):
    input_data = np.array([[spx, uso, slv, eur_usd]])
    prediction = model.predict(input_data)
    st.success(f"Predicted GLD Price: {prediction[0]:.2f}") 