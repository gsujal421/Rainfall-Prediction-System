🌧️ Rainfall Prediction System
This project delivers a robust, production-ready machine learning pipeline for binary classification (Rain/No Rain) using a highly optimized Random Forest model deployed via Streamlit. The key focus of this project was to overcome common real-world challenges—specifically data imbalance and model miscalibration—to ensure the application provides accurate, trustworthy probability predictions.

🚀 Solution Highlights
1. Robust Model Training
Data Handling: Addressed significant class imbalance through Downsampling the majority class, ensuring the model learned to recognize both Rain and No Rain events equally.

Optimization Metric: Model selection and hyperparameter tuning were driven by the F1-Weighted Score rather than misleading accuracy, ensuring balanced performance across classes.

2. Bias Correction via Calibration (The Core Fix)
The raw Random Forest model suffered from probability skew (predicting a 72% chance of rain on a dry day).

This was corrected using Isotonic Calibration (CalibratedClassifierCV) to adjust the model's confidence scores, making the output probabilities truly honest and reliable.

3. Deployment Integrity
The final decision boundary is set at a mathematically derived Optimal Threshold (0.667), which is necessary to maximize the F1-Score and prevent prediction errors that a standard 0.50 threshold would introduce.

All user inputs are correctly Scaled using the saved scaler.pkl before prediction, preventing data format mismatches.

💻 Project Structure
The repository contains the three essential components for this ML application:

notebook.ipynb: Contains the full data preprocessing pipeline, EDA, Downsampling, Hyperparameter Tuning, and the critical Model Calibration step. This notebook generates all artifacts.

app.py: The Streamlit application that handles the web UI, loads the calibrated artifacts, scales user input, and applies the custom threshold logic.

Deployment Artifacts (*.pkl, .txt):

best_model_calibrated.pkl

scaler.pkl

optimal_threshold.txt (Contains the value: 0.667)

⚙️ Future Plans
The project is structured for easy deployment and scaling:

Dockerization: The next step is to containerize the Streamlit application using Docker for consistent, platform-independent deployment.

Data Retraining: Implement a scheduled pipeline to periodically retrain the model with fresh data to account for seasonal and climate shifts.
