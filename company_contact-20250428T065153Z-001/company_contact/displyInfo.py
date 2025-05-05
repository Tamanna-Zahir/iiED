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

# Show all tables
cursor.execute("SHOW TABLES;")
tables = [row[0] for row in cursor.fetchall()]
print("\n📋 Available tables:")
for tbl in tables:
    print(f" - {tbl}")

# Keep asking for a valid table name
while True:
    table_name = input("\nEnter the table name to display: ").strip()
    cursor.execute("SHOW TABLES LIKE %s;", (table_name,))
    if cursor.fetchone():
        break
    else:
        print(f"❌ Table '{table_name}' does not exist. Please try again.")

# Get row count
cursor.execute(f"SELECT COUNT(*) FROM `{table_name}`;")
row_count = cursor.fetchone()[0]
print(f"\n📊 Total rows in '{table_name}': {row_count}")

# Paginate display
page_size = 10
offset = 0

while True:
    cursor.execute(f"SELECT * FROM `{table_name}` LIMIT {page_size} OFFSET {offset};")
    rows = cursor.fetchall()
    if not rows:
        print("No more data.")
        break
    columns = [desc[0] for desc in cursor.description]
    df_page = pd.DataFrame(rows, columns=columns)

    print(f"\n--- Showing rows {offset + 1} to {offset + len(rows)} ---")
    print(df_page)

    next_action = input("\nType 'n' for next page, 'e' to export, or any other key to exit: ").strip().lower()
    if next_action == 'n':
        offset += page_size
    elif next_action == 'e':
        export_format = input("Export as CSV or Excel? (csv/xlsx): ").strip().lower()
        export_name = input("Enter file name (without extension): ").strip()
        if export_format == "csv":
            df_all = pd.read_sql(f"SELECT * FROM `{table_name}`", connection)
            df_all.to_csv(f"{export_name}.csv", index=False)
            print(f"✅ Table exported to '{export_name}.csv'")
        elif export_format == "xlsx":
            df_all = pd.read_sql(f"SELECT * FROM `{table_name}`", connection)
            df_all.to_excel(f"{export_name}.xlsx", index=False)
            print(f"✅ Table exported to '{export_name}.xlsx'")
        else:
            print("❌ Invalid format. Export cancelled.")
        break
    else:
        break

# Close connection
cursor.close()
connection.close()
