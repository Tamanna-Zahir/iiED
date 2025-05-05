# 📦 MySQL Table Creator from CSV

This Python script allows you to create a MySQL table directly from a CSV file by importing its contents. It provides an interactive experience with input validation, error handling, and data cleaning to make database creation from spreadsheets smooth and reliable.

---

## 🚀 Features

- ✅ Accepts CSV files from any directory  
- ✅ Interactive prompt for custom MySQL table names  
- ✅ Checks and warns before overwriting existing tables  
- ✅ Automatically cleans column names (e.g., removes special characters)  
- ✅ Keeps asking for valid input instead of exiting on errors  

---

## 🛠️ Requirements

Make sure you have the following installed:

- Python 3.6 or higher  
- MySQL Server running locally  
- MySQL user with permissions to create tables and insert data  
- Required Python packages:

```bash
pip install pandas mysql-connector-python
```

## ⚙️ MySQL Configuration
This script connects to MySQL using the following credentials (set in the script):
- host="localhost"
- user="Tamanna"
- password="tam123"
- database="companydatabase"

## 📂 CSV File Guidelines

- To ensure smooth importing:
- File must be .csv format
- Should include a header row (used for column names)
- Ensure consistent formatting in each column
- Special characters in column names are removed automatically
- Spaces in column names are converted to underscores

## 💡 How to Use

1. Open your terminal or command prompt.
2. Run the script:
```
python main.py
```
3. Follow the prompts:
  - Enter the full path to your .csv file (e.g., C:/Users/You/data/employees.csv) 
  - Enter a table name you want to create in MySQL
  - If the table exists, you'll be asked whether you want to overwrite it
