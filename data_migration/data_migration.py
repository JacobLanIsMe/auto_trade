import logging
import sys
import os
from datetime import datetime

# Ensure the log directory exists
log_dir = r'C:\Logs\DataMigration'
os.makedirs(log_dir, exist_ok=True)
# Use current time as the log file name
log_filename = datetime.now().strftime('%Y%m%d_%H%M%S') + '.log'
logging.basicConfig(
    filename=os.path.join(log_dir, log_filename),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.sql_server_service import get_candidate_data as get_sql_data
from service.mongodb_service import delete_all_from_collection, get_candidate_data as get_mongo_data, insert_many_to_collection



def main():
    logging.info("Starting data migration process.")
    candidates = get_sql_data()
    delete_all_from_collection("Candidate")
    # Convert Candidate objects to dicts for MongoDB insertion
    candidate_dicts = [c.__dict__ for c in candidates]
    insert_many_to_collection("Candidate", candidate_dicts)
    logging.info("Data migration completed successfully.")
    # mongo_rows = get_mongo_data()
    # for row in mongo_rows:
    #     print(row)

if __name__ == "__main__":
    main()
