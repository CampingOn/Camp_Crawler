from database.mongo_client import get_mongo_collection

def save_to_mongo(campsite_data):
    collection = get_mongo_collection()
    for camp in campsite_data:
        collection.update_one({"_id": camp["_id"]}, {"$set": camp}, upsert=True)