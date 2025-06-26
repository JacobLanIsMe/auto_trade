import pyodbc

def get_candidate_data():
    # Update these variables with your SQL Server details
    server = 'localhost'  # or your server name
    # Example: server = 'localhost\\SQLEXPRESS'
    database = 'TwStockAutoTrade'
    # username = 'your_username'
    # password = 'your_password'

    # Connection string
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Candidate WHERE IsDeleted = 0')
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print('Error:', e)
        return []
