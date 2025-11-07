import pandas as pd
import os

# Load raw CSV
df = pd.read_csv("data/raw/owid-covid-data.csv")

# Index starts from 1
df.index = range(1, len(df) + 1)

# Keep only normal countries
df = df[df['iso_code'].str.match(r'^[A-Z]{3}$', na=False)]

# Keep only needed columns
columns_to_keep = ['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']
df = df[columns_to_keep]

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Replace NaN with 0 and convert floats to int
df.fillna(0, inplace=True)
float_cols = df.select_dtypes(include=['float']).columns
df[float_cols] = df[float_cols].astype(int)

# Drop duplicates
df = df.drop_duplicates(subset=['location','date'])

# Create folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save cleaned CSV
df.to_csv("data/processed/covid_clean.csv", index_label="index")
print("Clean CSV saved at data/processed/covid_clean.csv")

# Show first rows
print(df.head())
