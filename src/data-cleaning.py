import pandas as pd

# Load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Standardize column names and return the modified DataFrame
def standardize_column_names(df):
    # Standardize column names to lowercase and replace spaces with underscores
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

# Clean text fields in the DataFrame
def clean_text_fields(df):
    # Strip leading/trailing whitespace and convert text fields to lowercase
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        df[col] = df[col].str.strip().str.lower()
    return df

# Handle missing values in the DataFrame
def handle_missing_values(df):
    df = df.dropna(subset=['price', 'qty'])
    return df

