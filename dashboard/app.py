import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

# Set page config
st.set_page_config(page_title="HR Analytics Dashboard", page_icon="👥", layout="wide")

# Load data func
@st.cache_data
def load_data():
    data_path = 'data/cleaned_hr_data.csv'
    if not os.path.exists(data_path):
        st.error(f"Data file not found at {data_path}. Please run data_preprocessing.py first.")
        return None
    return pd.read_csv(data_path)

df = load_data()

if df is not None:
    # Sidebar Filters
    st.sidebar.header("Filter Data")
    
    # Department Filter
    departments = ["All"] + list(df['Department'].unique())
    selected_dept = st.sidebar.selectbox("Select Department", departments)
    
    # Gender Filter
    genders = ["All"] + list(df['Gender'].unique())
    selected_gender = st.sidebar.selectbox("Select Gender", genders)
    
    # Job Role Filter
    roles = ["All"] + list(df['Job Role'].unique())
    selected_role = st.sidebar.selectbox("Select Job Role", roles)
    
    # Apply Filters
    filtered_df = df.copy()
    if selected_dept != "All":
        filtered_df = filtered_df[filtered_df['Department'] == selected_dept]
    if selected_gender != "All":
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
    if selected_role != "All":
        filtered_df = filtered_df[filtered_df['Job Role'] == selected_role]

    st.title("👥 HR Analytics & Employee Attrition Dashboard")
    st.markdown("Analyze workforce performance and employee attrition risk factors.")

    # KPIs
    st.markdown("### Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    
    total_employees = len(filtered_df)
    attrition_rate = (filtered_df['Attrition_Encoded'].mean() * 100) if total_employees > 0 else 0
    avg_salary = filtered_df['Monthly Income'].mean() if total_employees > 0 else 0
    avg_tenure = filtered_df['Years at Company'].mean() if total_employees > 0 else 0
    
    col1.metric("Total Employees", f"{total_employees}")
    col2.metric("Attrition Rate", f"{attrition_rate:.1f}%")
    col3.metric("Avg Monthly Salary", f"${avg_salary:,.0f}")
    col4.metric("Avg Tenure", f"{avg_tenure:.1f} Yrs")
    
    st.markdown("---")
    
    # Visualizations
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### Attrition by Department")
        dept_attrition = filtered_df.groupby('Department')['Attrition_Encoded'].mean().reset_index()
        dept_attrition['Attrition Rate %'] = dept_attrition['Attrition_Encoded'] * 100
        fig1 = px.bar(dept_attrition, x='Department', y='Attrition Rate %', color='Department', title="Attrition Rate by Department")
        st.plotly_chart(fig1, use_container_width=True)
        
    with col_chart2:
        st.markdown("#### Attrition by Job Role")
        role_attrition = filtered_df.groupby('Job Role')['Attrition_Encoded'].mean().reset_index().sort_values(by='Attrition_Encoded', ascending=False)
        role_attrition['Attrition Rate %'] = role_attrition['Attrition_Encoded'] * 100
        fig2 = px.bar(role_attrition, x='Attrition Rate %', y='Job Role', orientation='h', color='Attrition Rate %', color_continuous_scale='Reds', title="Attrition Rate by Job Role")
        st.plotly_chart(fig2, use_container_width=True)
        
    col_chart3, col_chart4 = st.columns(2)
    
    with col_chart3:
        st.markdown("#### Salary vs Attrition")
        fig3 = px.box(filtered_df, x='Attrition', y='Monthly Income', color='Attrition', title="Monthly Income vs Attrition", category_orders={"Attrition": ["No", "Yes"]})
        st.plotly_chart(fig3, use_container_width=True)
        
    with col_chart4:
        st.markdown("#### Tenure vs Attrition")
        fig4 = px.box(filtered_df, x='Attrition', y='Years at Company', color='Attrition', title="Years at Company vs Attrition", category_orders={"Attrition": ["No", "Yes"]})
        st.plotly_chart(fig4, use_container_width=True)
        
    st.markdown("---")
    
    # Correlation Heatmap
    st.markdown("#### Correlation Matrix")
    numeric_df = filtered_df.select_dtypes(include=[np.number])
    if numeric_df.shape[1] > 0:
        corr_matrix = numeric_df.corr().round(2)
        fig_heat = px.imshow(corr_matrix, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', title="Correlation between features")
        st.plotly_chart(fig_heat, use_container_width=True)
    else:
        st.info("Not enough numeric columns for heatmap.")
        
    # Data Preview
    if st.checkbox("Show Raw Data"):
        st.write(filtered_df.head(100))
