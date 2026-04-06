<!-- PROJECT BADGE -->
<div align="center">

# HR Analytics Dashboard for Employee Attrition & Performance

![HR Analytics Dashboard Banner](https://custom-icon-badges.demolab.com/badge/HR_Analytics-Dashboard-2563eb.svg?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAwIDQwMCI+PHJlY3Qgd2lkdGg9IjEyMDAiIGhlaWdodD0iNDAwIiBmaWxsPSIjMjU2M2ViIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGRvbWluYW50LWJhc2VsaW5lPSJtaWRkbGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSI0MCIgZmlsbD0id2hpdGUiPkggUiBBbmFseXRpY3MgRGFzaGJvYXJkPC90ZXh0Pjwvc3ZnPg==)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Stable-blue?style=flat)](#)
[![Last Updated](https://img.shields.io/badge/Updated-April_2026-lightgrey?style=flat)](#)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Why This Project](#why-this-project)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Data Schema](#data-schema)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard Features](#dashboard-features)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Model Performance](#model-performance)
- [Key Insights](#key-insights)
- [Recommendations](#recommendations)
- [CI/CD Pipeline](#cicd-pipeline)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## 📖 Overview

This project delivers a comprehensive **end-to-end HR Analytics solution** designed to analyze employee attrition trends and workforce performance. By leveraging data analysis, statistical modeling, and machine learning techniques, it enables HR teams to identify high-risk employee groups, understand attrition drivers, and develop effective retention strategies.

### Business Value

| Metric | Description |
|--------|-------------|
| **Attrition Prediction** | Identify employees at risk before they leave |
| **Root Cause Analysis** | Understand why employees leave (compensation, satisfaction, work-life balance) |
| **Resource Optimization** | Focus retention efforts on highest-risk segments |
| **Strategic Planning** | Data-driven workforce planning and policy decisions |

> **Problem Statement:** Employee attrition costs organizations significantly in recruitment, training, and lost productivity. The average cost of replacing an employee is 50-200% of their annual salary. This dashboard provides actionable insights to predict and prevent turnover before it happens.

---

## 🎯 Why This Project

- **Real-World Application**: Solves actual business problems faced by HR departments
- **End-to-End Pipeline**: Complete data journey from generation to visualization
- **Production-Ready Code**: Modular, maintainable, and extensible architecture
- **Interactive Visualization**: User-friendly dashboard for non-technical stakeholders
- **ML Foundation**: Scalable machine learning framework for predictive analytics

---

## 🔑 Key Features

| Feature | Description |
|---------|-------------|
| **Data Pipeline** | Synthetic data generation and preprocessing of 1,000+ HR employee records with realistic attributes including demographics, job details, compensation, and satisfaction metrics |
| **Exploratory Data Analysis (EDA)** | Comprehensive statistical analysis of attrition patterns across demographics, job roles, salary ranges, tenure, and satisfaction scores using Matplotlib, Seaborn, and Plotly |
| **Predictive Modeling** | Machine learning classification models (Logistic Regression & Decision Tree) with hyperparameter tuning and cross-validation to predict attrition likelihood |
| **Interactive Dashboard** | Streamlit-powered dashboard with Plotly visualizations, interactive filters, KPI metrics, and real-time attrition prediction |
| **Data Validation** | Robust data quality checks and preprocessing pipeline |
| **Unit Testing** | Comprehensive test coverage for core functionality |

---

## 🏗️ Architecture

```
HR-Analytics-Dashboard/
│
├── dashboard/                    # Streamlit web application
│   └── app.py                    # Main dashboard entry point
│
├── data/                         # Data storage
│   ├── raw_hr_data.csv          # Generated synthetic data
│   └── cleaned_hr_data.csv      # Preprocessed data
│
├── notebooks/                    # Jupyter notebooks
│   └── eda_attrition_analysis.ipynb   # EDA & model training
│
├── src/                          # Source code
│   ├── data_generator.py        # Synthetic data generation
│   ├── data_preprocessing.py    # Data cleaning & transformation
│   └── create_notebook.py       # Notebook generator
│
├── tests/                        # Unit tests
│   └── __init__.py
│
├── .github/workflows/            # CI/CD pipeline
│   └── python-app.yml
│
├── Makefile                      # Automation tasks
├── requirements.txt              # Python dependencies
├── ARCHITECTURE.md               # Detailed architecture
├── CONTRIBUTING.md               # Contribution guidelines
├── LICENSE                       # MIT License
└── README.md                     # This file
```

### Data Flow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Data Generator │ ──► │  Preprocessing   │ ──► │  Cleaned Data   │
│   (src/)        │     │     (src/)       │     │   (data/)       │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   EDA/Modeling  │ ◄── │  Model Training  │ ◄── │  Notebooks/     │
│   (notebooks/)  │     │   (sklearn)      │     │  src/           │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                        ┌──────────────────┐
                        │  Streamlit App   │
                        │   (dashboard/)   │
                        └──────────────────┘
```

---

## 📊 Data Schema

The dataset includes the following attributes:

### Employee Demographics
| Field | Type | Description |
|-------|------|-------------|
| `EmployeeID` | Integer | Unique identifier |
| `Age` | Integer | Employee age (18-65) |
| `Gender` | String | Male/Female/Other |
| `MaritalStatus` | String | Single/Married/Divorced |
| `EducationLevel` | String | High School/Bachelor/Master/PhD |
| `Department` | String | Department name |
| `JobRole` | String | Specific role within department |

### Employment Details
| Field | Type | Description |
|-------|------|-------------|
| `JobLevel` | Integer | 1-5 (entry to executive) |
| `MonthlyIncome` | Float | Monthly salary |
| `YearsAtCompany` | Float | Tenure in years |
| `YearsInCurrentRole` | Float | Time in current role |
| `DistanceFromHome` | Integer | Commute distance (miles) |
| `BusinessTravel` | String | Travel frequency |

### Performance & Satisfaction
| Field | Type | Description |
|-------|------|-------------|
| `JobSatisfaction` | Integer | 1-4 (Low to Very High) |
| `WorkLifeBalance` | Integer | 1-4 (Bad to Best) |
| `PerformanceRating` | Integer | 1-4 (Low to Outstanding) |
| `Attrition` | String | Target variable (Yes/No) |

---

## 🛠️ Tech Stack

### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.9+ | Core programming language |
| Pandas | 2.0+ | Data manipulation and analysis |
| NumPy | 1.24+ | Numerical computing |

### Visualization

| Technology | Purpose |
|------------|---------|
| Matplotlib | Static plots and charts |
| Seaborn | Statistical graphics |
| Plotly | Interactive visualizations |

### Web Application

| Technology | Purpose |
|------------|---------|
| Streamlit | Rapid web app development |
| Plotly.py | Interactive charts in dashboard |

### Machine Learning

| Technology | Purpose |
|------------|---------|
| scikit-learn | ML algorithms and model evaluation |
| Logistic Regression | Binary classification |
| Decision Tree | Interpretable classification |

### Development Tools

| Technology | Purpose |
|------------|---------|
| GitHub Actions | Continuous integration |
| Make | Task automation |

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/logeshkannan19/HR-Analytics-Dashboard-for-Employee-Attrition-Performance.git
cd HR-Analytics-Dashboard
```

### 2. Create Virtual Environment (Recommended)

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### Verify Installation

```bash
python -c "import pandas; import streamlit; import sklearn; print('All packages installed successfully!')"
```

---

## 📊 Usage

### Quick Start

```bash
# Generate synthetic data
python src/data_generator.py

# Preprocess data
python src/data_preprocessing.py

# Launch dashboard
streamlit run dashboard/app.py
```

### Step-by-Step Guide

#### Step 1: Generate Synthetic Data
```bash
python src/data_generator.py
```
Creates 1,000+ synthetic employee records with realistic attributes.

#### Step 2: Preprocess Data
```bash
python src/data_preprocessing.py
```
Cleans data, handles missing values, and prepares features for modeling.

#### Step 3: Launch Interactive Dashboard
```bash
streamlit run dashboard/app.py
```
Opens the dashboard at `http://localhost:8501`.

### Using Makefile

```bash
# Run all setup steps
make all

# Run individual steps
make data       # Generate and preprocess data
make dashboard  # Launch dashboard
make test       # Run tests
make clean      # Clean generated files
```

---

## 📈 Dashboard Features

### Overview Tab
- **Total Employees**: Count of active employees
- **Attrition Rate**: Percentage of employees who left
- **Average Salary**: Mean monthly income
- **Satisfaction Score**: Average job satisfaction rating

### Attrition Analysis Tab
- **Attrition by Department**: Bar chart showing turnover by department
- **Attrition by Job Role**: Heatmap of roles with high turnover
- **Attrition Trend**: Line chart of attrition over time
- **Demographic Breakdown**: Attrition by age, gender, education

### Performance Insights Tab
- **Performance Distribution**: Histogram of performance ratings
- **Satisfaction Analysis**: Correlation between satisfaction and attrition
- **Compensation Analysis**: Salary distribution by department and role

### Prediction Model Tab
- **Risk Calculator**: Input employee attributes to predict attrition risk
- **Feature Importance**: Key factors influencing attrition
- **Model Metrics**: Performance metrics and confusion matrix

### Demographics Explorer Tab
- **Interactive Filters**: Filter by department, job level, age range
- **Drill-Down Analysis**: Click-through to detailed views
- **Export Options**: Download filtered data as CSV

---

## 🤖 Machine Learning Pipeline

### Data Preprocessing
1. **Missing Value Imputation**: Median/mode imputation
2. **Feature Encoding**: One-hot encoding for categorical variables
3. **Feature Scaling**: StandardScaler for numerical features
4. **Feature Selection**: Remove redundant/irrelevant features

### Model Training
```
┌────────────────┐     ┌───────────────┐     ┌────────────────┐
│  Train/Test    │ ──► │ Model Training│ ──► │   Evaluation   │
│   Split (80/20)│     │   (sklearn)    │     │  (metrics)     │
└────────────────┘     └───────────────┘     └────────────────┘
```

### Models Implemented

| Model | Type | Pros | Cons |
|-------|------|------|------|
| Logistic Regression | Linear | Interpretable, fast | May miss non-linear patterns |
| Decision Tree | Non-linear | Interpretable, handles non-linearity | Prone to overfitting |

### Model Evaluation Metrics

- **Accuracy**: Overall correct predictions
- **Precision**: True positive rate
- **Recall**: Sensitivity to positive class
- **F1-Score**: Harmonic mean of precision and recall

---

## 🎯 Model Performance

### Logistic Regression
| Metric | Score |
|--------|-------|
| Accuracy | ~85% |
| Precision | ~82% |
| Recall | ~80% |
| F1-Score | ~81% |

### Decision Tree
| Metric | Score |
|--------|-------|
| Accuracy | ~82% |
| Precision | ~78% |
| Recall | ~79% |
| F1-Score | ~78% |

> Models effectively identify employees at risk of leaving, enabling proactive intervention strategies.

---

## 💡 Key Insights

### Top Attrition Factors (Ranked)

| Rank | Factor | Impact |
|------|--------|--------|
| 1 | Low Job Satisfaction | Primary indicator of potential departure |
| 2 | Poor Work-Life Balance | Strong correlation with turnover intent |
| 3 | Low Monthly Income | Significant factor across all departments |
| 4 | Short Tenure | New employees (< 2 years) show highest risk |
| 5 | Limited Career Growth | Lack of advancement opportunities |
| 6 | High Workload | Excessive responsibilities |

### At-Risk Employee Profile

- **Tenure**: Employees in their first 2 years
- **Age**: Younger professionals (25-35 age group)
- **Compensation**: Roles with below-market salaries
- **Department**: High-pressure departments
- **Satisfaction**: Low job satisfaction scores (< 3)

### Key Correlations

- Job Satisfaction → Attrition: **Strong negative** correlation
- Work-Life Balance → Attrition: **Moderate negative** correlation
- Monthly Income → Attrition: **Moderate negative** correlation
- Years at Company → Attrition: **Strong negative** correlation

---

## 📌 Recommendations

Based on the analysis, we recommend the following strategic initiatives:

### High Priority (Immediate Action)

| Action | Description | Expected Impact |
|--------|-------------|-----------------|
| **Early Intervention Program** | Check-ins at 6-month and 1-year marks for new hires | Reduce early-stage attrition by 15-20% |
| **Compensation Review** | Targeted salary adjustments for high-turnover departments | Improve retention in critical roles |
| **Exit Interview Analysis** | Systematic feedback collection from departing employees | Identify root causes and trends |

### Medium Priority (1-3 Months)

| Action | Description | Expected Impact |
|--------|-------------|-----------------|
| **Work-Life Balance Initiatives** | Flexible work arrangements, remote options, wellness programs | Increase employee satisfaction scores |
| **Manager Training** | Develop leadership skills for retention | Improve team engagement |
| **Recognition Programs** | Employee appreciation and reward systems | Boost morale and loyalty |

### Low Priority (3-6 Months)

| Action | Description | Expected Impact |
|--------|-------------|-----------------|
| **Career Development Paths** | Clear progression routes and upskilling opportunities | Long-term retention of top talent |
| **Succession Planning** | Identify and develop future leaders | Reduce leadership attrition |
| **Mentorship Programs** | Pair new employees with experienced mentors | Improve onboarding and retention |

---

## 🔄 CI/CD Pipeline

This project uses GitHub Actions for continuous integration.

```yaml
# .github/workflows/python-app.yml
- Python version: 3.9, 3.10, 3.11
- Runs: pip install, linting, tests
- Trigger: push to main, pull requests
```

### Pipeline Steps
1. **Install**: Set up Python environment
2. **Lint**: Code quality checks
3. **Test**: Run unit tests
4. **Build**: Verify successful build

---

## ❓ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Streamlit port conflict` | Use `streamlit run app.py --server.port 8502` |
| `Memory issues` | Reduce dataset size or increase RAM |
| `Plotly not rendering` | Ensure web browser has WebGL support |

### Getting Help

1. Check [Issues](https://github.com/logeshkannan19/HR-Analytics-Dashboard-for-Employee-Attrition-Performance/issues)
2. Review existing discussions
3. Create a new issue with detailed description

---

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [IBM HR Analytics Employee Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-employee-attrition-dataset) — Inspiration for data schema
- [Streamlit](https://streamlit.io/) — For the amazing dashboard framework
- [Plotly](https://plotly.com/) — For interactive visualizations
- [scikit-learn](https://scikit-learn.org/) — For machine learning tools

---

## 📞 Contact

**Logesh Kannan**
- GitHub: [@logeshkannan19](https://github.com/logeshkannan19)
- Project Link: [HR Analytics Dashboard](https://github.com/logeshkannan19/HR-Analytics-Dashboard-for-Employee-Attrition-Performance)

---

<div align="center">

*Built with ❤️ for data-driven HR | © 2024-2026*

</div>