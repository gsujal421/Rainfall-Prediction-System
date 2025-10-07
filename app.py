import streamlit as st
import joblib
import numpy as np  
from numpy import loadtxt


page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://grist.org/wp-content/uploads/2022/07/GettyImages-592034559-1-e1658260204585.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed; /* Keeps the background from scrolling */
    background-repeat: no-repeat;
    /* FIX: Slightly darken the image for better text contrast */
    filter: brightness(0.85);
}}

[data-testid="stAppViewContainer"] > .main {{
    background-color: rgba(255, 255, 255, 0.85); /* 85% transparent white overlay */
    margin: 10px; 
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}}

[data-testid="stAppViewContainer"], h1, h2, h3, h4, .stMarkdown, .stText, label {{
    color: black !important;
}}

.stButton>button {{
    color: white !important;
}}

[data-testid="stAlert"] * {{
    color: black !important;
}}

[data-testid="stAlert"][role="alert"] {{
    background-color: #8B0000 !important; /* Dark Red (Maroon) */
    border-color: #8B0000 !important;
}}

[data-testid="stAlert"][role="alert"] + [data-testid="stAlert"][role="alert"] {{
    background-color: #FF8C00 !important; /* Dark Orange */
    border-color: #FF8C00 !important;
}}

[data-testid="stAlert"][role="alert"] h3, 
[data-testid="stAlert"][role="alert"] p, 
[data-testid="stAlert"][role="alert"] * {{
    color: white !important;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stSidebar"] {{
    background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

try:
    scaler=joblib.load('scaler.pkl')
    model=joblib.load('best_model_calibrated.pkl')
except FileNotFoundError:
    st.error("Error: Model file 'best_model_calibrated.pkl' not found. Please ensure it is in the same directory.")
    st.stop()

try:
    CUSTOM_THRESHOLD = loadtxt('optimal_threshold.txt').item()
except FileNotFoundError:
    CUSTOM_THRESHOLD = 0.667 


st.title("Rainfall Prediction System 🌧")
st.divider()

st.subheader("Rainfall Prediction System Overview")
st.write("This application provides a highly reliable forecast for the likelihood of rain tomorrow, " \
"based on seven key meteorological inputs (Pressure, Humidity, Wind Speed, etc.).")
st.divider()

st.header("Input Weather Parameters")
st.divider()

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


st.divider()

button=st.button('Predict')
if button:
    input_data = np.array([[pressure, dewpoint, humidity, cloud, sunshine, wind_direction, windspeed]])
    input_data_scaled = scaler.transform(input_data)
    probability_of_rain = model.predict_proba(input_data_scaled)[0][1]
    
    if probability_of_rain >= CUSTOM_THRESHOLD:
        st.error(f"🌧️ Prediction: It will rain tomorrow! (Probability: {probability_of_rain:.3f})")
        st.info("Carry an umbrella ☔")
    else:
        st.success(f"☀️ Prediction: No rain tomorrow! (Probability: {probability_of_rain:.3f})")
        st.balloons()
        st.info("Enjoy your day! 😎")

st.divider()
st.write("Developed by Sujal Gupta ")
st.write("[GitHub](https://github.com/gsujal421/Rainfall-Prediction-System)")