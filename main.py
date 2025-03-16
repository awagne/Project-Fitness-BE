from connect import collection

# Insert a document
collection.insert_one({"name": "Alice", "age": 25})

# Find a document
print(collection.find_one({"name": "Alice"}))