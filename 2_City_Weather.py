import streamlit as st
import requests
import json

st.title("🌆 City Weather")

# Load Indian cities from JSON
with open("indian_cities.json", "r", encoding="utf-8") as f:
    indian_cities = json.load(f)

city = st.selectbox("Select a city", indian_cities)

if city:
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        st.metric("Temperature", f"{data['main']['temp']} °C")
        st.metric("Humidity", f"{data['main']['humidity']}%")
        st.metric("Wind Speed", f"{data['wind']['speed']} m/s")
    else:
        st.error("City not found or API error.")
