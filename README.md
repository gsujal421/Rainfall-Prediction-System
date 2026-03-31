
Weather-Based Delivery Optimization System

A decision intelligence system that uses weather predictions to optimize delivery operations.
Goes beyond forecasting rain and translates weather into demand, delay, and operational decisions.

---

TL;DR
Predicts rainfall → Estimates delivery impact → Recommends actions
- Demand forecasting
- Delivery delay estimation
- Operational decision support

---

Key Business Impact
- Orders increase by 40% during high rainfall
- Delivery time increases by 75%
- Delay rate nearly 2x in heavy rain conditions

---

System Workflow

Weather Inputs → ML Model → Rain Probability → Impact Engine → Delivery Metrics → Recommendations

---

Core Components:

1. Weather Prediction Model
- Random Forest Classifier
- Probability Calibration (Isotonic)
- Threshold tuning using Precision-Recall
Ensures reliable probability output

2. Delivery Impact Engine
Maps rainfall probability to:
- Order demand
- Delivery time
- Delay percentage
Built using data-driven simulation and aggregation

3. Decision Recommendation System
- High Rain: Increase fleet, adjust ETA, pre-stock inventory
- Medium Rain: Add buffer, monitor demand
- Low Rain: Maintain normal operations

4. Interactive Dashboard
- Built with Streamlit
- Real-time prediction + business insights

---

Why This Matters

Weather disruptions impact delivery efficiency and customer experience.

This system enables proactive decision-making instead of reactive handling.

---

Tech Stack

Python, Scikit-learn, Pandas, NumPy, Streamlit, Matplotlib

---

How to Run
1. Clone repository
2. pip install -r requirements.txt
3. streamlit run app.py

---

## 📂 Project Structure

```bash
Weather-Delivery-Optimization-System/
├── app.py                     # Streamlit app (UI + predictions + insights)

├── data/                      # Datasets
│   ├── Rainfall.csv
│   └── delivery_data.csv

├── models/                    # Trained ML artifacts
│   ├── best_model_calibrated.pkl
│   ├── scaler.pkl
│   └── optimal_threshold.txt

├── notebooks/                 # Development & analysis
│   ├── weather_prediction_model_pipeline.ipynb
│   └── delivery_impact_analysis.ipynb

├── images/                    # UI assets & screenshots
│   ├── background.png
│   └── image.png

├── requirements.txt           # Dependencies
├── runtime.txt                # Python version (deployment)
├── Dockerfile                 # Containerization setup
├── .gitignore
├── LICENSE
└── README.md

---

Future Enhancements
- Real-time weather API integration
- AWS deployment
- Dynamic routing optimization

---

Author

Sujal Gupta

Demo: https://weather-delivery-optimization-system.streamlit.app/
