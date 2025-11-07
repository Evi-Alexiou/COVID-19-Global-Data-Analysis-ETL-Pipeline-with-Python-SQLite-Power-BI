import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("data/covid.db")

# Load cleaned data from the covid_data table
df = pd.read_sql("SELECT * FROM covid_data", conn)

# Keep only the latest date for each country
last_day = df.groupby("location")["date"].max().reset_index()
latest = df.merge(last_day, on=["location", "date"], how="inner")

# Select needed columns
final_df = latest[["location", "total_cases", "total_deaths"]]

# Convert numbers to integers
final_df[["total_cases", "total_deaths"]] = final_df[["total_cases", "total_deaths"]].fillna(0).astype(int)

# Save to CSV
final_df.to_csv("data/processed/covid_by_country.csv", index=False)
print("CSV file saved: data/processed/covid_by_country.csv")

# Save to SQLite
final_df.to_sql("covid_by_country", conn, if_exists="replace", index=False)
print("Table covid_by_country saved to SQLite database")

# Show sample
print(final_df.head())

# Close the connection
conn.close()


