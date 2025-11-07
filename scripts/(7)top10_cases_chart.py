import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("data/covid.db")

# Read all data from the 'covid_data' table
df = pd.read_sql("SELECT * FROM covid_data;", conn)

# Close the connection
conn.close()

# Compute the maximum total cases per country and take top 10
top_cases = df.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)

# Print top 10 countries with most COVID-19 cases
print("Top 10 countries with the most COVID-19 cases:")
print(top_cases)

# Create a bar chart
plt.figure(figsize=(10,6))
top_cases.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries with the Most COVID-19 Cases")
plt.ylabel("Total Cases")
plt.xlabel("Country")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
