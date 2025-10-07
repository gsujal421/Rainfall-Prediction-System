# 🌧 Rainfall Prediction System

An interactive **Streamlit web application** that predicts the **probability of rainfall** for the next day using key meteorological parameters such as **pressure, humidity, dewpoint, cloud cover, sunshine duration, wind direction, and wind speed**.

This project combines machine learning with a visually appealing interface and is designed for future deployment through **Docker**.

---

## 🚀 Features

- 🧠 **Machine Learning-Powered Prediction** – Uses a calibrated model to deliver accurate rainfall forecasts.  
- 🎨 **Elegant Streamlit Interface** – Includes background imagery and transparent overlays for a polished UI.  
- ⚙️ **Optimized Threshold** – Employs a fine-tuned decision threshold for balanced accuracy.  
- 💾 **Pre-Trained Model Integration** – Directly loads serialized model and scaler objects.  
- 🐳 **Docker-Ready Design** – Easily deployable in a containerized environment.

---

## 🧰 Tech Stack

| Category         | Tool             |
| ---------------- | ---------------- |
| Frontend         | Streamlit        |
| ML Framework     | Scikit-learn     |
| Language         | Python           |
| Containerization | Docker (planned) |
| Data Handling    | NumPy, Joblib    |

---

## How It Works

The app loads the scaler, calibrated ML model, and optimal threshold.

Users input seven key weather features.

The data is standardized and fed into the model.

The app outputs:

🌧️ “Rain expected tomorrow” — if probability ≥ threshold

☀️ “No rain tomorrow” — otherwise

---

## 📈 Machine Learning Overview

The model was trained and optimized using:

Data preprocessing and feature scaling

Model calibration for probability accuracy

Threshold tuning for F1-score optimization

---

