import os
import pymongo

def get_candidate_data():
    # Get MongoDB Atlas URI from environment variable
    uri = os.environ.get('MongoDb')
    if not uri:
        raise ValueError('MongoDb environment variable is not set.')
    try:
        client = pymongo.MongoClient(uri)
        db = client.MyFuture
        collection = db["Dividend"]
        rows = list(collection.find({"StockId": "2465"}))
        return rows
    except Exception as e:
        print('Error:', e)
        return []
