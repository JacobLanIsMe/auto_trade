import pyodbc
from model.Candidate import Candidate

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
            cursor.execute('SELECT Id, StockCode, CompanyName, PurchasedLot FROM Candidate WHERE IsDeleted = 0')
            rows = cursor.fetchall()
            candidates = []
            for row in rows:
                candidates.append(Candidate(
                    id=row.Id,
                    stockCode=row.StockCode,
                    companyName=row.CompanyName,
                    isHolding=row.PurchasedLot > 0
                ))
            return candidates
    except Exception as e:
        print('Error:', e)
        return []
