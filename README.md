# HR Analytics Dashboard for Employee Attrition & Performance

## Overview
This project is an end-to-end HR Analytics solution designed to analyze employee attrition trends and workforce performance. By applying data analysis and machine learning techniques, this project helps HR teams identify high-risk employee groups and improve retention strategies.

## Features
- **Data Pipeline:** Synthetic generation and preprocessing of HR employee records.
- **Exploratory Data Analysis (EDA):** Comprehensive analysis of attrition impacts across demographics, job roles, salary, and tenure.
- **Machine Learning Model:** A predictive classification model that estimates the likelihood of an employee leaving the company.
- **Interactive Dashboard:** A Streamlit-powered dashboard offering rich visualizations (using Plotly) and actionable KPIs to deep-dive into the dataset.

## Tech Stack
- **Languages/Core:** Python, Pandas, NumPy
- **Visualizations:** Matplotlib, Seaborn, Plotly
- **Web App:** Streamlit
- **Machine Learning:** Scikit-learn

## How to Run

1. **Install Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate & Preprocess Data:**
   Run the data scripts from the root directory to create the datasets inside the `data/` folder.
   ```bash
   python src/data_generator.py
   python src/data_preprocessing.py
   ```

4. **Run the Dashboard:**
   Start the interactive Streamlit dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```

## Key Insights
- **Model Performance:** The trained Machine Learning models (Logistic Regression & Decision Tree) can effectively predict potential attrition.
- **Top Attrition Factors:** Low Job Satisfaction, poor Work-Life Balance, and low Monthly Income are the strongest early indicators of an employee choosing to leave.
- **Tenure Risk:** Employees within their first 2 years at the company exhibit the highest attrition risk, particularly younger professionals.
- **HR Recommendations:** 
  1. Perform early interventions by checking in with new hires at the 6-month and 1-year marks.
  2. Implement compensation reviews for groups experiencing high turnover.
  3. Promote work-life balance initiatives to help retain experienced employees long-term.
