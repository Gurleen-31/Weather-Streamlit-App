import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json

st.title("📈 Temperature Graph")

# Load Indian cities from JSON
with open("indian_cities.json", "r", encoding="utf-8") as f:
    indian_cities = json.load(f)

city = st.selectbox("Select a city", indian_cities)

if city:
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    # For demonstration, we'll simulate past week's data
    dates = pd.date_range(end=pd.Timestamp.today(), periods=7).to_pydatetime().tolist()
    temperatures = [25 + i for i in range(7)]  # Dummy data
    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temperatures
    })
    fig = px.line(df, x="Date", y="Temperature", title=f"Past Week Temperature in {city}")
    st.plotly_chart(fig)
