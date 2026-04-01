# Roadmap: HR Analytics Dashboard

## 🚀 Current State (v1.0)
- End-to-end synthetic HR data generation.
- Data preprocessing & feature engineering on key attrition drivers.
- Exploratory Data analysis via Jupyter Notebooks.
- Interactive Streamlit Dashboard deployed locally.
- Basic prediction utilizing Logistic Regression and Decision Trees.

## 🔜 Next Steps (v1.1 - Upcoming)
- Implement caching to speed up large dataset visualizations in the dashboard.
- Export trained machine learning model parameters as localized `.pkl` files in the `models/` directory for Streamlit live predictions.
- Add additional filters in the Dashboard (Income levels, Tenure Groups).
- Setup PyTest suite and introduce basic unit testing for data transformers.

## 🌟 Future Goals (v2.0)
- Integrate a live backend database (e.g., PostgreSQL or SQLite) for data ingestion.
- Implement User Authentication for the Dashboard ensuring sensitive HR intel is secure.
- Add advanced Machine Learning (XGBoost / Random Forests) for better accuracy.
- Containerize the application through Docker for seamless deployment on AWS/GCP/Azure.
