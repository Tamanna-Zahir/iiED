import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="Tamanna",
    password="tam123",
    database="companydatabase"
)
cursor = connection.cursor()

# Keep prompting until a valid table name is entered
while True:
    # Always show available tables
    cursor.execute("SHOW TABLES;")
    tables = [row[0] for row in cursor.fetchall()]
    print("\n📋 Available tables:")
    for tbl in tables:
        print(f" - {tbl}")

    table_name = input("\nEnter the table name to search (e.g., contacts): ").strip()
    cursor.execute("SHOW TABLES LIKE %s;", (table_name,))
    if cursor.fetchone():
        break
    print(f"❌ Table '{table_name}' does not exist. Please try again.\n")

# Get columns from the selected table
try:
    cursor.execute(f"SHOW COLUMNS FROM `{table_name}`;")
    columns = [col[0] for col in cursor.fetchall()]
except Exception as e:
    print(f"Error fetching columns: {e}")
    cursor.close()
    connection.close()
    exit()

# Display columns to user
print("\n📑 Available fields:")
for idx, col in enumerate(columns, start=1):
    print(f"{idx}. {col}")

# Ask user to select a column by number
while True:
    try:
        choice = int(input("\nSelect a field number to filter by: "))
        if 1 <= choice <= len(columns):
            selected_column = columns[choice - 1]
            break
        else:
            print("❌ Invalid number. Please select a number from the list.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# Ask user for a search value
search_value = input(f"🔍 Enter the value to search for in '{selected_column}': ").strip()

# Execute query
try:
    query = f"SELECT * FROM `{table_name}` WHERE `{selected_column}` LIKE %s LIMIT 50;"
    cursor.execute(query, (f"%{search_value}%",))
    rows = cursor.fetchall()
    result_columns = [desc[0] for desc in cursor.description]
    df_result = pd.DataFrame(rows, columns=result_columns)

    if df_result.empty:
        print("\n🚫 No matching records found.")
    else:
        print("\n✅ --- Search Results ---")
        print(df_result)
except Exception as e:
    print(f"Query error: {e}")

cursor.close()
connection.close()
