# data_migration

This project demonstrates how to connect to a local SQL Server using Python and pyodbc.

## Setup
1. Activate your virtual environment:
   ```powershell
   .\venv\Scripts\Activate
   ```
2. Install dependencies (already installed):
   ```powershell
   pip install pyodbc
   ```
3. Update `get_sql_data.py` with your SQL Server credentials and table name.
4. Run the script:
   ```powershell
   python get_sql_data.py
   ```

## Notes
- Make sure you have the ODBC Driver 17 for SQL Server installed on your system.
- Use parameterized queries for production code to avoid SQL injection.
