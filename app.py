import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# Ensure the app can find the 'src' folder
sys.path.append(os.path.abspath(os.path.join('.')))
from src.forecasting import simulate_fi_trajectory

# Page Configuration
st.set_page_config(page_title="Ethiopia FI Forecast 2027", layout="wide", page_icon="🇪🇹")

st.title("🇪🇹 Ethiopia Financial Inclusion Simulator")
st.markdown("""
This dashboard simulates the impact of the **National Financial Inclusion Strategy (NFIS-II)**.
Adjust the sliders to see how policy delays or accelerations affect the 2027 goal.
""")

# --- Sidebar: Policy Levers ---
st.sidebar.header("Policy Impact Levers")
st.sidebar.info("Adjust the annual percentage lift expected from key initiatives.")

fayda_impact = st.sidebar.slider("Digital ID (Fayda) Annual Lift (%)", 0.0, 10.0, 7.0) / 100
interop_impact = st.sidebar.slider("Interoperability Annual Lift (%)", 0.0, 6.0, 4.0) / 100
baseline_growth = st.sidebar.slider("Organic Baseline Growth (%)", 1.0, 4.0, 2.5) / 100

# --- Calculations ---
start_val = 49.0  # Current 2024 Baseline
years = [2024, 2025, 2026, 2027]
drivers = {'fayda': fayda_impact, 'interop': interop_impact}

# Generate forecast
forecast_values = [start_val] + simulate_fi_trajectory(start_val, 3, baseline_growth, drivers)
final_val = forecast_values[-1]
target_gap = round(final_val - 70.0, 2)

# --- Layout: Key Metrics ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current (2024)", f"{start_val}%")
with col2:
    st.metric("Projected (2027)", f"{final_val}%", delta=f"{target_gap}% vs Target")
with col3:
    status = "✅ TARGET MET" if final_val >= 70 else "❌ TARGET MISSED"
    st.subheader(status)

# --- Visualization ---
st.divider()
chart_df = pd.DataFrame({
    'Year': years,
    'Projected Ownership': forecast_values,
    'National Target': [70.0] * 4
}).set_index('Year')

st.line_chart(chart_df, color=["#1f77b4", "#d62728"])

# --- Documentation Note ---
with st.expander("📌 Data Assumptions & Limitations"):
    st.write("""
    - **Baseline:** Assumes a current 49% ownership rate based on recent NBE estimates.
    - **Linearity:** Assumes policy impacts are distributed evenly over the 3-year period.
    - **Externalities:** Does not account for major macroeconomic shifts or hardware supply chain issues.
    """)