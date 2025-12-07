import pandas as pd

# Load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Standardize column names and return the modified DataFrame
def standardize_column_names(df):
    # Standardize column names to lowercase and replace spaces with underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
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

# remove rows with non-positive values in 'price' or 'qty'
def remove_non_positive_values(df):
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
    df = df[(df['price'] > 0) & (df['qty'] > 0)]
    return df

def main():
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_cleaned.csv"

    df_raw = load_data(raw_path)
    df_clean = standardize_column_names(df_raw)
    df_clean = clean_text_fields(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_non_positive_values(df_clean)
    df_clean.to_csv(cleaned_path, index=False)  
    print(f"Cleaned data saved to {cleaned_path}")

if __name__ == "__main__":
    main()