# HR Analytics Dashboard Architecture

## System Overview
The HR Analytics Dashboard is designed to be a lightweight, reproducible data pipeline and visualization application. It follows a modular architecture separating data ingestion, processing, modeling, and presentation layers.

### Directory Structure
```
├── src/           # Core Python source code functions
├── data/          # Raw and processed datasets
├── notebooks/     # Jupyter Notebooks for EDA and modeling experiments
├── models/        # Serialized ML models (Joblib/Pickle)
├── dashboard/     # Streamlit web application frontend
├── reports/       # Output analysis reports and metrics
├── tests/         # Unit and integration test suite
├── .github/       # CI/CD and GitHub Actions workflows
├── docs/          # Technical documentation
└── config/        # Environment and configuration files
```

### Components
1. **Data Pipeline (`src/`)**: Comprises generating the simulated datasets (`data_generator.py`) and robustly processing, cleaning, and engineering novel features (`data_preprocessing.py`).
2. **Exploratory Data Analysis (`notebooks/`)**: Features standalone analysis in Jupyter utilizing Matplotlib and Seaborn for deep statistical discovery and feature correlation.
3. **ML Modeling Pipeline**: Trains predictive models (Logistic Regression, Decision Trees) utilizing `scikit-learn` on employee factors like job satisfaction, salary, and tenure to identify attrition risk.
4. **Dashboard Frontend (`dashboard/app.py`)**: An elegant, interactive Streamlit frontend with Plotly elements for dynamic insights, empowering HR with live filtering and metrics.

### Technology Stack
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Plotly, Seaborn, Matplotlib
- **Machine Learning**: Scikit-Learn
- **Web App**: Streamlit
