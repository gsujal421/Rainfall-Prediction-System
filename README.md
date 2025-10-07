<p>🌧 Rainfall Prediction System</p>
<p>An interactive Streamlit web application that predicts the probability of rainfall for the next day using key meteorological parameters such as pressure, humidity, dewpoint, cloud cover, sunshine duration, wind direction, and wind speed.</p>
<p>This project combines machine learning with a visually appealing interface and is designed for future deployment through Docker.</p>
<p>🚀 Features</p>
<p>🧠 Machine Learning-Powered Prediction – Uses a calibrated model to deliver accurate rainfall forecasts.</p>
<p>🎨 Elegant Streamlit Interface – Includes background imagery and transparent overlays for a polished UI.</p>
<p>⚙️ Optimized Threshold – Employs a fine-tuned decision threshold for balanced accuracy.</p>
<p>💾 Pre-Trained Model Integration – Directly loads serialized model and scaler objects.</p>
<p>🐳 Docker-Ready Design – Easily deployable in a containerized environment.</p>
<p>Tech Stack
| Category         | Tool             |
| ---------------- | ---------------- |
| Frontend         | Streamlit        |
| ML Framework     | Scikit-learn     |
| Language         | Python           |
| Containerization | Docker (planned) |
| Data Handling    | NumPy, Joblib    |</p>
<p>🧩 Project Structure
Rainfall_Prediction_System/
│
├── app.py                      # Main Streamlit application
├── notebook.ipynb              # Model training and experimentation
├── best_model_calibrated.pkl   # Trained ML model
├── scaler.pkl                  # Data scaler for normalization
├── optimal_threshold.txt       # Tuned probability threshold
├── background.jpg              # Streamlit background image
├── requirements.txt            # Python dependencies
├── Dockerfile                  # (For future Docker deployment)
└── README.md                   # Project documentation</p>
<p>🌦 How It Works</p>
<p>The app loads the scaler, calibrated ML model, and optimal threshold.</p>
<p>Users input seven key weather features.</p>
<p>The data is standardized and fed into the model.</p>
<p>The app outputs:</p>
<p>🌧️ “Rain expected tomorrow” — if probability ≥ threshold</p>
<p>☀️ “No rain tomorrow” — otherwise</p>
<p>📈 Machine Learning Overview</p>
<p>The model was trained and optimized using:</p>
<p>Data preprocessing and feature scaling</p>
<p>Model calibration for probability accuracy</p>
<p>Threshold tuning for F1-score optimization.</p>
<p>👨‍💻 Developer</p>
<p>Developed by: Sujal Gupta</p>
<p>Optimized for both local and future Dockerized deployment.</p>
