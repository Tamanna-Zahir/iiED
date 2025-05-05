import pandas as pd
import mysql.connector
import os

# Keep asking for a valid file path
while True:
    file_path = input("Enter the full path to the CSV file: ").strip()
    if os.path.exists(file_path):
        break
    else:
        print(f"File '{file_path}' not found. Please try again.\n")

# Read CSV file
df = pd.read_csv(file_path, encoding="utf-8")
df.columns = df.columns.str.strip().str.replace(r"[^\w\s]", "", regex=True).str.replace(" ", "_")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost", user="Tamanna", password="tam123", database="companydatabase"
)
cur = conn.cursor()

# Keep asking for a valid table name
while True:
    table_name = input("Enter the desired MySQL table name: ").strip()
    cur.execute("SHOW TABLES LIKE %s", (table_name,))
    if cur.fetchone():
        confirm = input(f"Table '{table_name}' already exists. Overwrite it? (yes/no): ").strip().lower()
        if confirm == "yes":
            cur.execute(f"DROP TABLE IF EXISTS `{table_name}`;")
            break
        else:
            print("Please enter a different table name.\n")
    else:
        break

# Create table
columns = ", ".join(f"`{col}` TEXT" for col in df.columns)
cur.execute(f"CREATE TABLE `{table_name}` ({columns});")

# Insert data
placeholders = ", ".join(["%s"] * len(df.columns))
insert_sql = f"INSERT INTO `{table_name}` VALUES ({placeholders})"
for _, row in df.iterrows():
    cur.execute(insert_sql, tuple(row.astype(str)))

conn.commit()
cur.close()
conn.close()

print(f"Table '{table_name}' created and data inserted successfully.")
