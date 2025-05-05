# 🏢 iiED Company Database Management System

This project is developed for **iiED (International Institute for Entrepreneurial Development)** to serve as a foundational tool for managing structured company data using a **relational MySQL database** and **Python-based interface scripts**.

The system enables users to:
- Import data from CSV files into MySQL
- View table content with pagination and export options
- Search/filter records by any field in any table

---

## 📌 Project Objective

To streamline the process of managing company contact data by:
- Creating a reusable and easy-to-use system for database population
- Providing accessible tools to query and explore relational data
- Enabling data preview and export without needing SQL expertise

---

## 🧰 Technologies Used

- **Programming Language**: Python 3.x  
- **Database**: MySQL (local server)  
- **Python Libraries**:
  - `pandas` – data handling and table formatting  
  - `mysql-connector-python` – MySQL integration  
  - `openpyxl` – Excel file support (for optional export)

---

## 🗂️ Project Structure

| Script             | Purpose                                                        |
|--------------------|----------------------------------------------------------------|
| `main.py`          | Imports `.csv` files and creates corresponding MySQL tables    |
| `displayInfo.py`   | Views table contents with pagination and export (CSV/XLSX)     |
| `query_tool.py`    | Searches any table by any field using partial matching         |
| `README/`          | Contains extended documentation for each script                |

---

## 📁 Documentation Folder

All extended guides are organized inside a dedicated `README/` folder:

- `README/main.md` – Full project overview  
- `README/import_guide.md` – Instructions for importing CSV data (`main.py`)  
- `README/viewing_guide.md` – Guide for viewing and exporting table data (`displayInfo.py`)  
- `README/query_guide.md` – Guide for filtering/searching data (`query_tool.py`)  

This keeps the root clean and allows docs to scale with the project.

---

## ⚠️ CSV File Requirements

To ensure your data is imported correctly:

- The file **must be in `.csv` format** — other formats like `.xlsx` or `.txt` are **not supported**
- Must include a **header row** — the first row should contain column names
- Column names should:
  - Avoid special characters (e.g., `@`, `#`, `/`)
  - Be automatically cleaned (spaces become underscores, punctuation is removed)
- All rows should have a consistent number of columns
- Values must be plain text — date and numeric formats are stored as text by default

> Example:
> ```csv
> id,first_name,last_name,email
> 1,John,Doe,john@example.com
> 2,Mary,Smith,mary@example.com
> ```

---

## ⚙️ Database Configuration

The system connects to a MySQL server using the following default credentials:

```python
host = "localhost"
user = "Tamanna"
password = "tam123"
database = "companydatabase"

```
  You must **create the database manually** in your MySQL server before running the scripts.
  
## 🛠️ Setup Instructions
**1. Clone the repository:**
```
git clone https://github.com/Tamanna-Zahir/iiED.git
cd iiED
```

**2. Install dependencies:**
```
pip install pandas mysql-connector-python openpyxl
```

**3. Ensure MySQL is running locally**, and that the `companydatabase` schema exists.  
If it doesn't, create it in your MySQL server:
```
CREATE DATABASE companydatabase;
```

**4. Run the scripts as needed:**

- **To import a `.csv` file into MySQL:**
  ```
  python main.py
  ```

- **To view table content with pagination and export options:**
  ```
  python displayInfo.py
  ```

- **To search/filter records in a table by any field:**
  ```
  python query_tool.py
  ```

## 💡 User Experience Summary

- All scripts are interactive — they ask for user input (file paths, table names, field selections)
- Validation is built-in:
  - Invalid table names will prompt you again
  - Invalid field selections are handled gracefully
- You can preview data before exporting
- You can export full tables or query results to **CSV or Excel** formats

---

## 🔒 Credentials & Security

⚠️ This is an internal project for development or demonstration use.  
Do **not hardcode sensitive credentials** in production environments.

For secure deployments:

- Use environment variables
- Use a `.env` file or configuration manager
- Restrict access to MySQL by role and permissions

---

## 📈 Future Enhancements

- Auto-detect column data types (e.g., `INT`, `DATE`, `TEXT`)
- Web-based interface using **Flask** or **Streamlit**
- CSV validator before importing
- Role-based user authentication and access control

---

## 📬 Author

**Tamanna Zahir**  
For support or contributions, please open an issue or submit a pull request.

---

## 📄 License

This project is internal to **iiED** and is not publicly licensed for redistribution.
