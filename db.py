from flask import Flask, request, jsonify
from pymongo import MongoClient

import pymongo
from bson import ObjectId

app = Flask(__name__)

from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["mydatabase"]
# collection = db["mycollection"]

client = MongoClient("mongodb://localhost:27017/")  # Change the connection string as needed
db = client["UC_DB"]
use_case_list_collection = db["use_case_list"]

# Connect to the MongoDB server
# client = pymongo.MongoClient("mongodb://localhost:27017")

# Access the database and collection
# db = client.my_database
# collection = db.my_collection

# Define the document's ObjectId and the array field name
document_id = ObjectId("654a20e5f8a0191d0bf52918")
array_name = "list_of_usecases"

# Find the document by ObjectId
document = use_case_list_collection.find_one({"_id": document_id})
print(document)
if document:
    # Check if the array exists and has elements
    if array_name in document and len(document[array_name])>=0:
        # Retrieve the nested object from index 0
        nested_object_at_index_0 = document[array_name][0]
        if "value1" in nested_object_at_index_0:
            value1 = nested_object_at_index_0["value1"]
            value2 = nested_object_at_index_0["value2"]
            print("Value1:", value1)
            print("Value2:", value2)
        else:
            print("Nested object at index 0 does not contain 'value1'.")
    else:
        print(f"The array '{array_name}' is either missing or empty in the document.")
else:
    print(f"Document with ObjectId '{document_id}' not found.")


# Query to retrieve documents with a specific "application" value
# query = {"ID":'UC01'}
# Define the query
# query = {
#     "list_of_usecases.ID":"UC01"
# }

# result = use_case_list_collection.find(query)

# pipeline = [
#     # {
#     #     "$match": {"list_of_usecases.ID":"UC01"}
#     # },
#        {
#         "$project": {
#             "_id": '654a20e5f8a0191d0bf52918',  # Exclude the _id field
#             # "_id": "$list_of_usecases.ID"
#             "value_at_0": {"$arrayElemAt": ["$list_of_usecases", 0]}
#         }
#        }
# ]
# result = use_case_list_collection.aggregate(pipeline)

# # Print the result
# for document in result:
#     print(document)







# # @app.route("/add", methods=["POST"])
# # def add_data():
# #     data = request.json  # Assuming you're sending JSON data in the request
# #     collection.insert_one(data)
# #     return jsonify({"message": "Data saved to MongoDB"})

# # query = {"application": "HRMS"}

# # # Use the find() method to execute the query
# # results = collection.find(query)

# # # Loop through the results and print specific values
# # for result in results:
# #     print("Application:", result["application"])
# #     print("Industry:", result["industry"])
    
# # if __name__ == "__main__":
# #     app.run(debug=True, port='8001')
