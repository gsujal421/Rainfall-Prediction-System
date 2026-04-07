# 🌧 Weather-Based Delivery Optimization System

🔗 **Live Demo:** https://weather-delivery-optimization-system.streamlit.app/

Developed a data-driven decision system to quantify how rainfall impacts delivery demand and delays, identifying 40% increase in demand and 75% rise in delays during high rainfall conditions.

Analyzed 50,000+ weather and delivery records to quantify the impact of rainfall on logistics performance.

---

## 📊 Problem Statement

Logistics and delivery companies face significant operational challenges during adverse weather conditions, especially rainfall.

Unexpected spikes in demand combined with delivery delays can lead to:
- Poor customer experience
- Operational inefficiencies
- Increased costs

This project aims to analyze weather patterns and quantify their impact on delivery performance to support better decision-making.

---

## ⚙️ Solution Approach

- Collected and processed weather and delivery datasets
- Built and calibrated a Random Forest model with threshold tuning to improve prediction reliability and align outputs with business impact
- Integrated delivery data to analyze operational impact
- Identified correlations between rainfall, demand, and delivery delays
- Applied threshold tuning to improve classification performance and align predictions with business impact
- Developed a system to translate predictions into actionable insights

---

## 🛠 Tech Stack

- Python (Pandas, NumPy, Scikit-learn)
- Machine Learning (Random Forest)
- Data Analysis & Visualization
- Streamlit (for interactive app)

---

## 📈 Key Insights

- High rainfall conditions led to ~40% increase in order demand
- Delivery delays increased by ~75% during peak rainfall
- Demand spikes and delays occur simultaneously, stressing operations
- Weather conditions are a strong external factor affecting logistics performance

---

## 🚀 Business Impact

- Enables delivery companies to anticipate demand surges
- Helps optimize workforce and delivery capacity planning
- Supports proactive decision-making during adverse weather
- Reduces delays and improves customer satisfaction

---

## 🧠 System Workflow

Weather Data → ML Prediction → Demand & Delay Analysis → Business Insights → Operational Decisions

---

## 📱 Application (Streamlit)

- Built an interactive dashboard to:
  - Input weather conditions
  - View predicted rainfall impact
  - Analyze delivery performance metrics

---
## 📸 Application Preview

![Dashboard](images/image.png)
 
---
## 🎯 Operational Recommendations

- Increase delivery fleet capacity during high rainfall periods to handle ~40% demand surge
- Allocate buffer time and dynamic routing to mitigate ~75% delay increase
- Prioritize high-value orders during peak weather disruptions

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
```

---
## 🚀 Future Improvements

- Integrate real-time weather API
- Deploy system on AWS for scalability
- Automate end-to-end data pipeline

---

Author

Sujal Gupta
