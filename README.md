<!-- PROJECT BADGE -->
<div align="center">

# HR Analytics Dashboard for Employee Attrition & Performance

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2+-orange.svg)](https://scikit-learn.org/)
[![Last Updated](https://img.shields.io/badge/Last_Updated-April_2026-lightgrey.svg)](#)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard Preview](#dashboard-preview)
- [Model Performance](#model-performance)
- [Key Insights](#key-insights)
- [Recommendations](#recommendations)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

This project delivers an **end-to-end HR Analytics solution** designed to analyze employee attrition trends and workforce performance. By leveraging data analysis and machine learning techniques, it enables HR teams to identify high-risk employee groups and develop effective retention strategies.

> **Problem Statement:** Employee attrition costs organizations significantly in recruitment, training, and lost productivity. This dashboard provides actionable insights to predict and prevent turnover before it happens.

---

## 🔑 Key Features

| Feature | Description |
|---------|-------------|
| **Data Pipeline** | Synthetic data generation and preprocessing of 1,000+ HR employee records with realistic attributes |
| **Exploratory Data Analysis (EDA)** | Comprehensive analysis of attrition patterns across demographics, job roles, salary ranges, and tenure |
| **Predictive Modeling** | Machine learning classification models (Logistic Regression & Decision Tree) to predict attrition likelihood |
| **Interactive Dashboard** | Streamlit-powered dashboard with Plotly visualizations and actionable KPIs |

---

## 🏗️ Architecture

```
HR-Analytics-Dashboard/
├── dashboard/           # Streamlit web application
│   └── app.py           # Main dashboard entry point
├── data/                # Data storage
│   ├── raw_hr_data.csv  # Generated synthetic data
│   └── cleaned_hr_data.csv  # Preprocessed data
├── notebooks/           # Jupyter notebooks for EDA & modeling
├── src/                 # Source code
│   ├── data_generator.py    # Synthetic data generation
│   ├── data_preprocessing.py  # Data cleaning & transformation
│   └── create_notebook.py   # Notebook generator
├── tests/               # Unit tests
├── Makefile             # Automation tasks
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🛠️ Tech Stack

### Languages & Frameworks
- **Python 3.9+** — Core programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing

### Visualization
- **Matplotlib** — Static plotting
- **Seaborn** — Statistical graphics
- **Plotly** — Interactive visualizations

### Web Application
- **Streamlit** — Rapid web app development

### Machine Learning
- **scikit-learn** — ML algorithms and model evaluation

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/logeshkannan19/HR-Analytics-Dashboard-for-Employee-Attrition-Performance.git
cd HR-Analytics-Dashboard
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📊 Usage

### Step 1: Generate Synthetic Data
```bash
python src/data_generator.py
```

### Step 2: Preprocess Data
```bash
python src/data_preprocessing.py
```

### Step 3: Launch Interactive Dashboard
```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

---

## 📈 Dashboard Preview

The interactive dashboard provides:

- **Overview Tab**: Key metrics (Total Employees, Attrition Rate, Average Salary)
- **Attrition Analysis**: Visual breakdown of attrition by department, role, and demographics
- **Performance Insights**: Employee performance distribution and satisfaction scores
- **Prediction Model**: Real-time attrition risk prediction for individual employees
- **Demographics Explorer**: Interactive filters for deep-dive analysis

---

## 🎯 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | ~85% | ~82% | ~80% | ~81% |
| Decision Tree | ~82% | ~78% | ~79% | ~78% |

> Models effectively identify employees at risk of leaving, enabling proactive intervention.

---

## 💡 Key Insights

### Top Attrition Factors
1. **Low Job Satisfaction** — Primary indicator of potential departure
2. **Poor Work-Life Balance** — Strong correlation with turnover intent
3. **Low Monthly Income** — Significant factor across all departments
4. **Short Tenure** — New employees (< 2 years) show highest risk

### At-Risk Profile
- Employees in their first 2 years
- Younger professionals (25-35 age group)
- Roles with high workload and low compensation
- Departments with limited growth opportunities

---

## 📌 Recommendations

Based on the analysis, we recommend the following strategies:

| Priority | Action Item | Expected Impact |
|----------|-------------|-----------------|
| 🔴 High | **Early Intervention Program** — Check-ins at 6-month and 1-year marks for new hires | Reduce early-stage attrition by 15-20% |
| 🔴 High | **Compensation Review** — Targeted salary adjustments for high-turnover departments | Improve retention in critical roles |
| 🟡 Medium | **Work-Life Balance Initiatives** — Flexible work arrangements, wellness programs | Increase employee satisfaction scores |
| 🟢 Low | **Career Development** — Clear progression paths and upskilling opportunities | Long-term retention of top talent |

---

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Logesh Kannan**  
- GitHub: [@logeshkannan19](https://github.com/logeshkannan19)
- Project Link: [HR Analytics Dashboard](https://github.com/logeshkannan19/HR-Analytics-Dashboard-for-Employee-Attrition-Performance)

---

<div align="center">

*Built with ❤️ for data-driven HR*

</div>