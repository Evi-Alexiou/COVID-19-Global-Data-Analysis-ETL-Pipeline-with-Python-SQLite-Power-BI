import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("data/covid.db")

# Load the covid_by_country table
df = pd.read_sql("SELECT * FROM covid_by_country", conn)

# Calculate total cases and total deaths
total_cases = df["total_cases"].sum()
total_deaths = df["total_deaths"].sum()

# Print the results
print("Global COVID-19 Summary (by country):")
print(f"Total Cases: {total_cases:,.0f}")
print(f"Total Deaths: {total_deaths:,.0f}")

# Close the database connection
conn.close()

