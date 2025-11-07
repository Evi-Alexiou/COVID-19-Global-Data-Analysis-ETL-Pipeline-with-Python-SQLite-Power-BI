import pandas as pd
import sqlite3

# File paths
csv_path = "data/processed/covid_clean.csv"
db_path = "data/covid.db"

# Load the cleaned CSV
df = pd.read_csv(csv_path)

# Create a connection to the SQLite database
conn = sqlite3.connect(db_path)

# Save the DataFrame as a table named 'covid_data'
df.to_sql("covid_data", conn, if_exists="replace", index=False)

# Example query: show first 5 rows
print(pd.read_sql("SELECT * FROM covid_data LIMIT 5;", conn))

# Example query: Top 10 countries with the most deaths
query = """
SELECT location, MAX(total_deaths) AS deaths
FROM covid_data
GROUP BY location
ORDER BY deaths DESC
LIMIT 10;
"""
print("\nTop 10 countries with most deaths:")
print(pd.read_sql(query, conn))

# Check total number of rows in the database
rows = pd.read_sql("SELECT COUNT(*) AS total_rows FROM covid_data;", conn)
print(f"\nTotal rows in the database: {rows['total_rows'][0]}")

# Close the database connection
conn.close()



