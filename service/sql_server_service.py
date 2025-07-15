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
            query = 'SELECT a.Id as Id, a.StockCode as StockCode, a.CompanyName as CompanyName, a.PurchasedLot as PurchasedLot, a.GapUpHigh as GapUpHigh, a.GapUpLow as GapUpLow, b.TechData as TechData FROM Candidate a JOIN StockTech b ON a.StockCode = b.StockCode WHERE a.IsDeleted = 0'
            cursor.execute(query)
            rows = cursor.fetchall()
            candidates = []
            for row in rows:
                candidates.append(Candidate(
                    id=row.Id,
                    stockCode=row.StockCode,
                    companyName=row.CompanyName,
                    isHolding=row.PurchasedLot > 0,
                    gapUpHigh=row.GapUpHigh,
                    gapUpLow=row.GapUpLow,
                    techData=row.TechData
                ))
            return candidates
    except Exception as e:
        print('Error:', e)
        return []
