import pandas as pd

# URL of the CSV file from GitHub
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

# Load CSV into a DataFrame
df = pd.read_csv(url)

# Show the first rows
print(df.head(10))

# Save CSV locally
df.to_csv("data/raw/owid-covid-data.csv", index=False)
print("CSV saved locally!")

