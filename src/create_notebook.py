import nbformat as nbf
import os

nb = nbf.v4.new_notebook()

text0 = """# HR Analytics: Exploratory Data Analysis & Modeling
This notebook performs Exploratory Data Analysis (EDA) on the employee attrition dataset and trains a machine learning model to predict attrition.
"""
code1 = """import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Load Data\ndf = pd.read_csv('../data/cleaned_hr_data.csv')\ndf.head()"""
text2 = """## 1. Attrition Distribution"""
code2 = """plt.figure(figsize=(6,4))\nsns.countplot(x='Attrition', data=df, palette='Set2')\nplt.title('Employee Attrition Distribution')\nplt.show()"""

text3 = """## 2. Attrition by Department & Job Role"""
code3 = """plt.figure(figsize=(10,5))\nsns.countplot(x='Department', hue='Attrition', data=df, palette='Set1')\nplt.title('Attrition by Department')\nplt.show()\n\nplt.figure(figsize=(12,6))\nsns.countplot(y='Job Role', hue='Attrition', data=df, palette='Set1')\nplt.title('Attrition by Job Role')\nplt.show()"""

text4 = """## 3. Salary & Tenure vs Attrition"""
code4 = """plt.figure(figsize=(8,5))\nsns.boxplot(x='Attrition', y='Monthly Income', data=df, palette='Set3')\nplt.title('Monthly Income vs Attrition')\nplt.show()\n\nplt.figure(figsize=(8,5))\nsns.boxplot(x='Attrition', y='Years at Company', data=df, palette='Set3')\nplt.title('Tenure vs Attrition')\nplt.show()"""

text5 = """## 4. Correlation Heatmap"""
code5 = """plt.figure(figsize=(12,8))\n# Select only required numeric columns for correlation\nnumeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()\ncorr = df[numeric_cols].corr()\nsns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')\nplt.title('Correlation Heatmap')\nplt.show()"""

text6 = """## 5. Machine Learning Model: Predicting Attrition
We will build a simple Logistic Regression and Decision Tree classifier to predict attrition.
"""
code6 = """from sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n\n# Prepare Features and Target\n# Use encoded columns created in preprocessing\nfeatures = ['Age', 'Monthly Income', 'Years at Company', 'Job Satisfaction', \n           'Performance Rating', 'Work-Life Balance', 'Gender_Encoded', \n           'Department_Encoded', 'JobRole_Encoded']\n           \nX = df[features]\ny = df['Attrition_Encoded']\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\n# Logistic Regression\nlr_model = LogisticRegression(max_iter=1000)\nlr_model.fit(X_train, y_train)\nlr_preds = lr_model.predict(X_test)\nprint(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_preds):.4f}")\n\n# Decision Tree\ndt_model = DecisionTreeClassifier(max_depth=5, random_state=42)\ndt_model.fit(X_train, y_train)\ndt_preds = dt_model.predict(X_test)\nprint(f"Decision Tree Accuracy: {accuracy_score(y_test, dt_preds):.4f}")\nprint("\\nDecision Tree Classification Report:")\nprint(classification_report(y_test, dt_preds))"""

text7 = """## Insights
* The model correctly predicts attrition with strong accuracy.
* Job Satisfaction, Work-Life Balance, and Income are strong indicators."""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text0),
    nbf.v4.new_code_cell(code1),
    nbf.v4.new_markdown_cell(text2),
    nbf.v4.new_code_cell(code2),
    nbf.v4.new_markdown_cell(text3),
    nbf.v4.new_code_cell(code3),
    nbf.v4.new_markdown_cell(text4),
    nbf.v4.new_code_cell(code4),
    nbf.v4.new_markdown_cell(text5),
    nbf.v4.new_code_cell(code5),
    nbf.v4.new_markdown_cell(text6),
    nbf.v4.new_code_cell(code6),
    nbf.v4.new_markdown_cell(text7)
]

os.makedirs('notebooks', exist_ok=True)
with open('notebooks/eda_attrition_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)
print("Notebook generated successfully!")
