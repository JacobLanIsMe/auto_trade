import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.sql_server_service import get_candidate_data as get_sql_data
from service.mongodb_service import delete_all_from_collection, get_candidate_data as get_mongo_data, insert_many_to_collection

def main():
    candidates = get_sql_data()
    delete_all_from_collection("Candidate")
    # Convert Candidate objects to dicts for MongoDB insertion
    candidate_dicts = [c.__dict__ for c in candidates]
    insert_many_to_collection("Candidate", candidate_dicts)
    # mongo_rows = get_mongo_data()
    # for row in mongo_rows:
    #     print(row)

if __name__ == "__main__":
    main()
