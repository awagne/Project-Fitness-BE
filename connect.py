from pymongo import MongoClient

# Connect to the MongoDB server running locally
client = MongoClient("mongodb://localhost:27017/")

# Access a database (it will be created if it doesn’t exist)
db = client["Project-Fitness"]

# Access a collection (equivalent to a table in relational databases)
collection = db["Users"]
