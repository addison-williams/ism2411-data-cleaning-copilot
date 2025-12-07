import pandas as pd

# Load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Standardize column names and return the modified DataFrame
def standardize_column_names(df):
    # Standardize column names to lowercase and replace spaces with underscores
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df