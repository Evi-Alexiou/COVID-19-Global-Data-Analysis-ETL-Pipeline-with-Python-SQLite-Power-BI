# COVID-19 Data Analysis Project

## Overview

This project provides a comprehensive workflow to collect, clean, process, analyze, and visualize COVID-19 data at a country level using **Python**, **SQLite**, and **Power BI**.  

It includes:
 
- Python scripts for each step of the ETL (Extract, Transform, Load) and analysis  
- Visualizations in Python (matplotlib)  
- Power BI dashboard exported as PDF  

The workflow demonstrates skills in **data extraction, cleaning, transformation, database management, aggregation, visualization, and reporting**.

---

## Dataset

The project uses the **Our World in Data COVID-19 dataset**, publicly available here:

- [Our World in Data - COVID-19 Dataset](https://github.com/owid/covid-19-data)

Key features include:

- `iso_code`, `location`, `date`, `total_cases`, `new_cases`, `total_deaths`, `new_deaths`, etc.  
- Global coverage of COVID-19 statistics  
- Updated regularly and publicly accessible

---

## Python Scripts & Workflow

The project follows a **full ETL and analysis workflow**:

### 1. `extract_data.py`
- Downloads the raw CSV from **Our World in Data** public source  
- Saves it to `data/raw/owid-covid-data.csv`  
- Ensures folder creation if not exists  

### 2. `transform_data.py`
- Loads raw CSV  
- Filters **only countries** (ISO codes with 3 letters)  
- Keeps only required columns: `location`, `date`, `total_cases`, `new_cases`, `total_deaths`, `new_deaths`  
- Converts dates to `datetime`, NaN to 0, floats to integers  
- Removes duplicates  
- Saves cleaned CSV to `data/processed/covid_clean.csv`  

### 3. `load_data_toSQLite.py`
- Loads cleaned CSV  
- Creates **SQLite database** `data/covid.db`  
- Saves DataFrame as table `covid_data`  
- Example queries: show first 5 rows, top 10 countries by deaths, total number of rows  

### 4. `creation_of_new_DF.py`
- Connects to SQLite table `covid_by_country`  
- Keeps the latest date per country  
- Aggregates total cases and deaths  
- Saves final CSV `data/processed/covid_by_country.csv` and updates table in SQLite  
- Prints print a few rows of the table  

### 5. `total_cases_globally.py`
- Connects to the SQLite database (`data/covid.db`)  
- Reads the `covid_by_country` table  
- Calculates **global totals** for COVID-19 cases and deaths  
- Prints a clear summary in the console for a quick overview  

### 6. `top10_cases_chart.py`
- Connects to SQLite  
- Extracts top 10 countries by **total cases**  
- Creates bar chart using matplotlib  

### 7. `top10_deaths_chart.py`
- Connects to SQLite  
- Extracts top 10 countries by **total deaths**  
- Creates bar chart using matplotlib  

---

## Power BI Dashboard

- A **Power BI dashboard** was created using the processed CSV and SQLite data  
- Key metrics visualized: top countries by cases/deaths, trends over time  
- Exported as PDF and included in `insights-dashboard/script_of_cases.pdf`    

---

## Requirements

Python 3.10+ recommended. 
 
Install dependencies:

pip install -r requirements.txt

---

## Skills Demonstrated

This project showcases the following skills:

- **Python Programming:** pandas for data manipulation, matplotlib for visualization  
- **ETL Processes:** extract, transform, and load workflows for datasets  
- **Data Cleaning:** handling missing values, type conversion, filtering, and deduplication  
- **Database Management:** SQLite integration and table creation  
- **Data Aggregation & Analysis:** grouping, summarizing, and generating key metrics  
- **Visualization:** charts for top countries by cases and deaths  
- **Reporting:** Power BI dashboard exported to PDF for sharing insights  
- **Project Organization:** modular scripts, reproducible workflow, GitHub best practices 
