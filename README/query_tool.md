# 🔍 Query MySQL Table by Field (`query_tool.py`)

This interactive Python script allows you to **search within a specific column** of a MySQL table using partial text matching. It’s designed to be user-friendly by guiding the user through available tables and fields, and it won’t crash on bad input — it just asks again.

---

## 🚀 Features

- ✅ Displays all available tables in the database
- ✅ Validates table name input and reprompts if incorrect
- ✅ Shows a numbered list of all fields (columns) in the selected table
- ✅ Lets user filter by any field using partial match (`LIKE`)
- ✅ Displays up to 50 matching rows in a clean table format
- ✅ Built-in error handling for bad inputs

---

## 🛠️ Requirements

Make sure the following are installed:

- Python 3.6 or higher
- A MySQL server running locally
- A database named `companydatabase`
- Python packages:

```bash
pip install pandas mysql-connector-python
```
## ⚙️ MySQL Configuration

This script connects to MySQL using the following credentials:

```
host = "localhost"
user = "Tamanna"
password = "tam123"
database = "companydatabase"
```
  💡 Change these values in the script to match your local MySQL setup.

##  💡 How to Use

1. Open your terminal or command prompt.
2. Run the script:
```
python query_tool.py
```
3. Follow the prompts:
- The script will list all tables in the companydatabase database.
- Enter a valid table name when prompted.
- The script will then list all columns (fields) in that table.
- Choose a field by its number and enter a search value.
- Results matching that value (partially) will be displayed.

## 📋 Example 

```
📋 Available tables:
 - contacts
 - companyrecords
 - contactdata

Enter the table name to search (e.g., contacts): contactdata

📑 Available fields:
1. id
2. first_name
3. email

Select a field number to filter by: 3
🔍 Enter the value to search for in 'email': gmail

✅ --- Search Results ---
       id   first_name         email
0       1   John             john@gmail.com
1       4   Mary             mary@gmail.com
```


## 📝 Notes

- Search uses LIKE '%value%', which allows for partial matching anywhere in the field.
- Limited to 50 results to prevent overload — you can change this limit in the script.
- All results are shown using Pandas in a clean table format.

## ✨ Future Enhancements (Suggestions)

- Export query results to CSV or Excel
- Add support for exact match or advanced filters (e.g., ranges)
- Allow chaining of multiple filters
- Add pagination and sorting support


