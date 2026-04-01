import pandas as pd
import numpy as np
import os

def generate_synthetic_hr_data(num_samples=2000, output_path='data/raw_hr_data.csv'):
    """
    Generates a synthetic HR dataset for employee attrition and performance analysis.
    """
    np.random.seed(42)
    
    # Employee ID
    employee_ids = [f'EMP{str(i).zfill(4)}' for i in range(1, num_samples + 1)]
    
    # Age (normal distribution between 22 and 60)
    ages = np.random.randint(22, 60, size=num_samples)
    
    # Gender
    genders = np.random.choice(['Male', 'Female', 'Non-Binary'], size=num_samples, p=[0.55, 0.40, 0.05])
    
    # Department
    departments = np.random.choice(['Sales', 'Research & Development', 'Human Resources', 'IT', 'Finance'], size=num_samples, p=[0.3, 0.4, 0.05, 0.15, 0.1])
    
    # Job Role based on Department
    job_roles = []
    for dept in departments:
        if dept == 'Sales':
            job_roles.append(np.random.choice(['Sales Executive', 'Sales Representative', 'Manager']))
        elif dept == 'Research & Development':
            job_roles.append(np.random.choice(['Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Manager']))
        elif dept == 'Human Resources':
            job_roles.append(np.random.choice(['HR Partner', 'Recruiter', 'Manager']))
        elif dept == 'IT':
            job_roles.append(np.random.choice(['Software Engineer', 'Data Analyst', 'IT Support', 'Manager']))
        else: # Finance
            job_roles.append(np.random.choice(['Financial Analyst', 'Accountant', 'Manager']))
            
    # Years at Company (exponential distribution to simulate right skew, capped at age - 18)
    years_at_company = np.clip(np.random.exponential(scale=5.0, size=num_samples).astype(int), 0, ages - 18)
    
    # Monthly Income based on role/tenure slightly
    monthly_incomes = []
    for role, years in zip(job_roles, years_at_company):
        if 'Manager' in role or 'Director' in role:
            base = np.random.randint(10000, 20000)
        elif 'Engineer' in role or 'Scientist' in role or 'Analyst' in role:
            base = np.random.randint(6000, 12000)
        else:
            base = np.random.randint(3000, 8000)
        monthly_incomes.append(base + (years * 200)) # Bonus based on tenure
        
    # Job Satisfaction (1 to 4)
    job_satisfaction = np.random.choice([1, 2, 3, 4], size=num_samples, p=[0.2, 0.2, 0.3, 0.3])
    
    # Performance Rating (1 to 4) - heavily weighted to 3 out of 4 (typically "meets expectations")
    performance_rating = np.random.choice([1, 2, 3, 4], size=num_samples, p=[0.05, 0.15, 0.6, 0.2])
    
    # Work-Life Balance (1 to 4)
    work_life_balance = np.random.choice([1, 2, 3, 4], size=num_samples, p=[0.1, 0.2, 0.4, 0.3])
    
    # Attrition Logic (synthetic likelihood)
    # Higher risk if: low satisfaction, low income, low work life balance, low performance or young tenure (except managers)
    attrition_probs = []
    for age, dept, inc, sat, perf, bal, tenure in zip(ages, departments, monthly_incomes, job_satisfaction, performance_rating, work_life_balance, years_at_company):
        risk = 0.1 # base
        if sat <= 2: risk += 0.2
        if bal <= 2: risk += 0.15
        if inc < 5000: risk += 0.1
        if perf <= 2: risk += 0.1
        if tenure <= 2 and age < 30: risk += 0.1
        
        # Managers leave less
        if inc > 12000: risk -= 0.15
        
        risk = np.clip(risk, 0.05, 0.95)
        attrition_probs.append(risk)
        
    attrition = [np.random.choice(['Yes', 'No'], p=[p, 1-p]) for p in attrition_probs]

    # Create DataFrame
    df = pd.DataFrame({
        'Employee ID': employee_ids,
        'Age': ages,
        'Gender': genders,
        'Department': departments,
        'Job Role': job_roles,
        'Monthly Income': monthly_incomes,
        'Years at Company': years_at_company,
        'Job Satisfaction': job_satisfaction,
        'Performance Rating': performance_rating,
        'Work-Life Balance': work_life_balance,
        'Attrition': attrition
    })
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Generated {num_samples} HR records and saved to {output_path}")
    
if __name__ == "__main__":
    generate_synthetic_hr_data()
