import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Service.sql_server_service import get_candidate_data as get_sql_data
from Service.mongodb_service import get_candidate_data as get_mongo_data

def main():
    print('--- SQL Server Data ---')
    sql_rows = get_sql_data()
    for row in sql_rows:
        print(row)

    print('\n--- MongoDB Data ---')
    mongo_rows = get_mongo_data()
    for row in mongo_rows:
        print(row)

if __name__ == "__main__":
    main()
