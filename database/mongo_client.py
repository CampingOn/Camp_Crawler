from pymongo import MongoClient
from config.settings import MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME

def get_mongo_collection():
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB_NAME]
        print(f"Connected to MongoDB database: {MONGO_DB_NAME}")
        return db[MONGO_COLLECTION_NAME]
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise

def save_to_mongo(campsite_data):
    collection = get_mongo_collection()
    for camp in campsite_data:
        # MongoDB에 저장 (upsert를 사용하여 중복 데이터 방지)
        collection.update_one({"_id": camp["_id"]}, {"$set": camp}, upsert=True)