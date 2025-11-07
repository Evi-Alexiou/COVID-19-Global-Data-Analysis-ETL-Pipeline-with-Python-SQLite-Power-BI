import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("data/covid.db")

# Read all data from the 'covid_data' table
df = pd.read_sql("SELECT * FROM covid_data;", conn)

# Close the connection
conn.close()

# Compute the maximum total deaths per country and take top 10
top_deaths = df.groupby('location')['total_deaths'].max().sort_values(ascending=False).head(10)

# Print top 10 countries with most COVID-19 deaths
print("Top 10 countries with the most COVID-19 deaths:")
print(top_deaths)

# Create a bar chart
plt.figure(figsize=(10,6))
top_deaths.plot(kind='bar', color='salmon')
plt.title("Top 10 Countries with the Most COVID-19 Deaths")
plt.ylabel("Total Deaths")
plt.xlabel("Country")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
