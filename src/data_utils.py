import pandas as pd
import os

def load_and_clean_data(file_path):
    """Loads FI data and applies standard cleaning with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        # Standardize dates
        df['observation_date'] = pd.to_datetime(df['observation_date'])
        # Filter for national-level baseline to avoid double-counting
        df_clean = df[(df['gender'] == 'all') & (df['location'] == 'national')]
        return df_clean
    except Exception as e:
        print(f"Error during data processing: {e}")
        return None

def calculate_growth_metrics(df, indicator='ACC_OWNERSHIP'):
    """Calculates Year-over-Year growth rates for a specific indicator."""
    try:
        subset = df[df['indicator_code'] == indicator].sort_values('observation_date')
        subset['pct_change'] = subset['value_numeric'].pct_change() * 100
        return subset
    except KeyError:
        print(f"Indicator {indicator} not found in dataset.")
        return pd.DataFrame()