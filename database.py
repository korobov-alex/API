from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

# Establishing connection to MongoDB
client = MongoClient("mongodb+srv://admin:admin@nosqlproject.3ixtayc.mongodb.net/?retryWrites=true&w=majority"
                     "&appName=NoSQLProject")

# Selecting the database
database = client.rest_db

# Collection for main data
connection = database["NoSQLProject"]

# Collection for history of changes
history_connection = database["HistoryOfChanges"]


# Function to update data in the history database
async def update_data_in_second_database(data_id, updated_data):
    # Getting current datetime
    current_datetime = datetime.now()

    # Checking if data with given ID exists in history database
    old_data = history_connection.find_one({"_id": ObjectId(data_id)})

    # If data doesn't exist, create new entry
    if not old_data:
        new_data = {
            "_id": ObjectId(data_id),
            "history": [{"timestamp": current_datetime, "data": updated_data}]
        }
        history_connection.insert_one(new_data)
    # If data exists, update existing entry
    else:
        history_connection.update_one(
            {"_id": ObjectId(data_id)},
            {"$push": {"history": {"timestamp": current_datetime, "data": updated_data}}}
        )
