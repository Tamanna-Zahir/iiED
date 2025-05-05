# 🧾 Display Table Info from MySQL (`displayInfo.py`)

This script connects to a MySQL database and allows you to **view and interact with table data**. It includes smart features such as showing available tables, paginated previews, and the ability to export table data to CSV or Excel files.

---

## 🚀 Features

- ✅ Lists all available tables before prompting for input  
- ✅ Prompts the user for a valid table name and checks if it exists  
- ✅ Displays total number of rows in the selected table  
- ✅ Previews table data in pages of 10 rows at a time  
- ✅ Option to export full table data to CSV or Excel  
- ✅ Keeps prompting until a valid table is provided  

---

## 🛠️ Requirements

Make sure you have the following installed:

- Python 3.6 or higher
- A running MySQL server
- A database named `companydatabase`
- Python packages:

```bash
pip install pandas mysql-connector-python
```
## ⚙️ MySQL Configuration
The script connects using the following credentials (update if needed):
```
host = "localhost"
user = "Tamanna"
password = "tam123"
database = "companydatabase"
```
  💡 Change these in the script if your MySQL configuration is different.

## 💡 How to Use

1. Open your terminal or command prompt.
2. Run the script:
```
python displayInfo.py
```
3. Follow the prompts:
  - See the list of available tables
  - Enter a valid table name
  - View paginated data (10 rows at a time)
  - Choose to:
  - Go to the next page (n)
    - Export the entire table to CSV or Excel (e)
    - Exit the preview

## 📋 Example

```
📋 Available tables:
 - employees
 - contacts
 - customer_orders

Enter the table name to display: contacts

📊 Total rows in 'contacts': 124

--- Showing rows 1 to 10 ---
   ID     Name       Email
   1      John Doe   john@example.com
   2      Jane Doe   jane@example.com
   ...

Type 'n' for next page, 'e' to export, or any other key to exit: e
Export as CSV or Excel? (csv/xlsx): csv
Enter file name (without extension): contact_export
✅ Table exported to 'contact_export.csv'
```
## 📌 Notes

- Pagination uses SQL LIMIT and OFFSET to retrieve rows in chunks
- Export includes all rows, not just what's previewed
- Column headers and formatting are preserved in exported files




   
