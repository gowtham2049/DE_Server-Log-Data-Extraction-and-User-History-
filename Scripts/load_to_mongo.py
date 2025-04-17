from pymongo import MongoClient
from config import MONGO_URL
import logging 


def load_mongo(data,db_name="guvi_db", collection_name="user_history"):
    logging.info("mongo connection")
    formatted_data = [{"email": email, "date": date} for email, date in data]
    client = MongoClient(MONGO_URL) 
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(formatted_data)
    logging.info("inserting into mongo db")