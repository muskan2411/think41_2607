import pandas as pd
from pymongo import MongoClient
import os

# MongoDB connection (local instance)
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]

def load_csv_to_mongodb(file_path, collection_name):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    df = df.where(pd.notnull(df), None)  # Replace NaNs with None

    data = df.to_dict(orient="records")

    collection = db[collection_name]
    collection.delete_many({})  # Optional: Clear old data
    result = collection.insert_many(data)

    print(f"✅ Loaded {len(result.inserted_ids)} records into '{collection_name}'")

if __name__ == "__main__":
    load_csv_to_mongodb("backend/data/distribution_centers.csv", "products")
    load_csv_to_mongodb("backend/data/inventory_items.csv", "customers")
    load_csv_to_mongodb("backend/data/orders.csv", "orders")
    load_csv_to_mongodb("backend/data/products.csv", "customers")
    load_csv_to_mongodb("backend/data/users.csv", "orders")
    load_csv_to_mongodb("backend/data/order_items.csv", "orders")
