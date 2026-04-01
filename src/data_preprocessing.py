import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder

def preprocess_data(input_path='data/raw_hr_data.csv', output_path='data/cleaned_hr_data.csv'):
    """
    Cleans the raw HR dataset and creates useful features.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"{input_path} not found. Please run data_generator.py first.")
        
    print(f"Reading raw data from {input_path}...")
    df = pd.read_csv(input_path)
    
    # 1. Handle Missing Values
    # Data is synthetic so we might not have NaNs, but for robustness:
    df.fillna(method='ffill', inplace=True)
    
    # 2. Convert Data Types
    df['Age'] = df['Age'].astype(int)
    df['Monthly Income'] = df['Monthly Income'].astype(int)
    df['Years at Company'] = df['Years at Company'].astype(int)
    
    # 3. Create New Features
    
    # Tenure Groups
    def assign_tenure_group(years):
        if years <= 2: return '0-2 Yrs'
        elif years <= 5: return '3-5 Yrs'
        elif years <= 10: return '6-10 Yrs'
        else: return '10+ Yrs'
    
    df['Tenure Group'] = df['Years at Company'].apply(assign_tenure_group)
    
    # Income Bands
    def assign_income_band(income):
        if income < 5000: return 'Low (<5k)'
        elif income < 10000: return 'Medium (5k-10k)'
        elif income < 15000: return 'High (10k-15k)'
        else: return 'Very High (15k+)'
        
    df['Income Band'] = df['Monthly Income'].apply(assign_income_band)
    
    # Encode categorical variables for ML modeling later (Optional for EDA, but good to have)
    # We will keep the original text columns and create encoded ones.
    
    le = LabelEncoder()
    df['Attrition_Encoded'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
    df['Gender_Encoded'] = le.fit_transform(df['Gender'])
    df['Department_Encoded'] = le.fit_transform(df['Department'])
    df['JobRole_Encoded'] = le.fit_transform(df['Job Role'])

    # Save to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data with new features saved to {output_path}")

if __name__ == "__main__":
    preprocess_data()
