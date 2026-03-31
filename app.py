import streamlit as st
import joblib
import numpy as np  
from numpy import loadtxt
import pandas as pd
import base64


@st.cache_data
def load_data():
    return pd.read_csv("data/delivery_data.csv")
df = load_data()


def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64("images/background.png") 

page_bg_img = f"""
<style>

/* Background Image (PURE — no filters) */
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Main Content Container (light readable panel) */
[data-testid="stAppViewContainer"] > .main {{
    background-color: rgba(255, 255, 255, 0.35);
    padding: 25px;
    border-radius: 12px;
    margin: 15px;
}}

/* Text Styling (clean + readable) */
h1, h2, h3, h4, h5, h6 {{
    color: #111 !important;
    font-weight: 600;
}}

p, label, div {{
    color: #222 !important;
    font-weight: 500;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Weather-Based Delivery Optimization System 🌧📦")

try:
    scaler = joblib.load('models/scaler.pkl')
    model = joblib.load('models/best_model_calibrated.pkl')
except FileNotFoundError:
    st.error("Error: Model file 'best_model_calibrated.pkl' not found. Please ensure it is in the same directory.")
    st.stop()

try:
    CUSTOM_THRESHOLD = loadtxt('models/optimal_threshold.txt')
except Exception:
    CUSTOM_THRESHOLD = 0.667

def get_metrics(prob):
    if prob > 0.7:
        data = df[df["rain_prob"] > 0.7]
    elif prob > 0.4:
        data = df[(df["rain_prob"] > 0.4) & (df["rain_prob"] <= 0.7)]
    else:
        data = df[df["rain_prob"] <= 0.4]
    
    if len(data) == 0:
        return {"orders": 0, "delivery_time": 0, "delay_pct": 0}

    return {
        "orders": int(data["orders"].mean()),
        "delivery_time": int(data["delivery_time"].mean()),
        "delay_pct": round(data["delay_pct"].mean()*100, 1)
    }



st.subheader("System Overview")

st.write(
    "This application predicts the probability of rainfall using key meteorological inputs "
    "and translates it into actionable business insights for delivery operations. "
    "By analyzing the impact of weather conditions on order demand, delivery time, and delays, "
    "the system helps optimize logistics, improve efficiency, and support data-driven decision-making."
)

st.header("Input Weather Parameters")

col1,col2=st.columns(2)

with col1:
    st.subheader("Moisture & Pressure")
    pressure= st.number_input("Enter the pressure (hPa):",min_value=990.0,max_value=1050.0,value=1013.0)
    dewpoint= st.number_input("Enter the dewpoint (°C):",min_value=-10.0,max_value=30.0,value=15.0)
    humidity= st.number_input("Enter the humidity (%):",min_value=30.0,max_value=100.0,value=50.0)
    cloud = st.number_input("Enter the cloud cover (%):",min_value=0.0,max_value=100.0,value=50.0)

with col2:
    st.subheader("Sunlight & Wind")
    sunshine= st.number_input("Enter the sunshine duration (hours):",min_value=0.0,max_value=24.0,value=12.0)
    wind_direction= st.number_input("Enter the wind direction (degrees):",min_value=5.0,max_value=360.0,value=180.0)
    windspeed= st.number_input("Enter the wind speed (m/s):",min_value=1.0,max_value=80.0,value=20.0)



button = st.button('Predict')

if button:
    input_df = pd.DataFrame([{
    "pressure": pressure,
    "dewpoint": dewpoint,
    "humidity": humidity,
    "cloud": cloud,
    "sunshine": sunshine,
    "winddirection": wind_direction,
    "windspeed": windspeed
}])
    input_df = input_df[scaler.feature_names_in_]
    input_data_scaled = scaler.transform(input_df)
    probability_of_rain = model.predict_proba(input_data_scaled)[0][1]

    # 🔹 Prediction Result
    if probability_of_rain >= CUSTOM_THRESHOLD:
        st.error(f"🌧️ Prediction: It will rain tomorrow! (Probability: {probability_of_rain:.3f})")
        st.info("Carry an umbrella ☔")
    else:
        st.success(f"☀️ Prediction: No rain tomorrow! (Probability: {probability_of_rain:.3f})")
        st.balloons()
        st.info("Enjoy your day! 😎")

    # 🔹 Business Impact
    st.subheader("📦 Delivery Impact Analysis")

    if probability_of_rain > 0.7:
        st.warning("⚠️ High Impact Expected")
        st.write("• Orders likely to increase by 30–40%")
        st.write("• Delivery time may increase significantly")
        st.write("• High risk of delays and cancellations")

    elif probability_of_rain > 0.4:
        st.info("Moderate operational impact expected")
        st.write("• Slight increase in demand")
        st.write("• Minor delivery delays possible")

    else:
        st.success("Normal delivery conditions")
        st.write("• Stable demand")
        st.write("• Minimal delays expected")

    # 🔹 Recommendations
    st.subheader("🚀 Recommended Actions")
    
    if probability_of_rain > 0.7:
        st.write("✔ Increase delivery fleet by 20–30%")
        st.write("✔ Adjust estimated delivery times (ETA)")
        st.write("✔ Pre-stock high demand items")
    
    elif probability_of_rain > 0.4:
        st.write("✔ Monitor demand closely")
        st.write("✔ Add delivery buffer time")
    else:
        st.write("✔ Maintain normal operations")
    
    # 🔹 Metrics (ALWAYS SHOWN)
    st.subheader("📊 Expected Operational Metrics")
    
    metrics = get_metrics(probability_of_rain)
    
    st.write(f"• Avg Orders: {metrics['orders']}")
    st.write(f"• Avg Delivery Time: {metrics['delivery_time']} mins")
    st.write(f"• Delay Rate: {metrics['delay_pct']}%")
    
st.write("Developed by Sujal Gupta ")
st.write("[GitHub](https://github.com/gsujal421/Rainfall-Prediction-System)")