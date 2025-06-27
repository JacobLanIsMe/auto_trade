import os
import pymongo
import logging

def get_candidate_data():
    try:
        collection = get_collection("Candidate")
        rows = list(collection.find({}))  # Get all documents from the collection
        return rows
    except Exception as e:
        logging.error('Error:', e)
        return []

def delete_all_from_collection(collection_name):
    try:
        collection = get_collection(collection_name)
        result = collection.delete_many({})
        print(f'Deleted {result.deleted_count} documents from {collection_name} collection.')
    except Exception as e:
        print('Error:', e)

def insert_many_to_collection(collection_name, data):
    try:
        collection = get_collection(collection_name)
        result = collection.insert_many(data)
        print(f'Inserted {len(result.inserted_ids)} documents into {collection_name} collection.')
    except Exception as e:
        print('Error:', e)

def get_collection(collection_name):
    # Get MongoDB Atlas URI from environment variable
    uri = os.environ.get('MongoDb')
    if not uri:
        raise ValueError('MongoDb environment variable is not set.')    
    client = pymongo.MongoClient(uri)
    db = client.MyFuture
    collection = db[collection_name]
    return collection