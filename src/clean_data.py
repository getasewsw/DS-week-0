import pandas as pd

# Load the CSV file
file_path = '../data/togo-dapaong_qc.csv'  # Adjust the path if necessary
df = pd.read_csv(file_path)

# Drop the "Comments" column
df_cleaned = df.drop(columns=["Comments"])

# Convert "Timestamp" to datetime
df_cleaned['Timestamp'] = pd.to_datetime(df_cleaned['Timestamp'])

# Remove any rows with negative values in "GHI", "DNI", and "DHI"
columns_to_check = ["GHI", "DNI", "DHI"]
for col in columns_to_check:
    df_cleaned = df_cleaned[df_cleaned[col] >= 0]

# Remove any duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('../data/cleaned_togo-dapaong_qc.csv', index=False)
