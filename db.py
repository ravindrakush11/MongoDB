from flask import Flask, request, jsonify
from pymongo import MongoClient
import pymongo
from bson import ObjectId
import pymongo.errors

app = Flask(__name__)

try:
    client = MongoClient("mongodb://localhost:27017/")  # Change the connection string as needed
    db = client["Dummy_db"]
    dummy = db["dummy"]
    print("Connected to MongoDB")
except pymongo.errors.ConnectionFailure:
    print("Failed to connect to MongoDB")

# client = MongoClient("mongodb://localhost:27017/")  # Change the connection string as needed
# db = client["UC_DB"]
# use_case_list_collection = db["use_case_list"]


output = { "my_array": [
        {"key1": "value1", "key2": "value2"},
        {"key1": "value3", "key2": "value4"}
    ]
    
}
object_id = 'a101'
dummy.insert_one(output, object_id)
client.close()





# criteria = {
#     "application": "HRMS",
#     "industry": "e-commerce",
#     "region": "india",
#     "_id": ObjectId("654a20e5f8a0191d0bf52918")
# }

# # Find the document matching the criteria
# result = use_case_list_collection.find_one(criteria)

# if result:
#     document_id = result["_id"]
#     print("Document ID:", document_id)
    
#     my_array = result.get("list_of_usecases", [])
    
#     for item in my_array:
#         id = item.get("ID")
#         title = item.get("title")
#         description = item.get('description')
#         print("id:", id)
#         print("title:", title)
#         print("description:", description)
        
        # print(item)
        
     
    # print("Application:", result["application"])
    # print("Industry:", result["industry"])
    # print("Region:", result["region"])
    # print("ID:", result["id"])
# else:
#     print("Document not found")

# Close the MongoDB connection
# client.close()
