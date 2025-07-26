from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["conversational_ai"] 


users = db["users"]
orders = db["orders"]
order_items = db["order_items"]
products = db["products"]
inventory_items = db["inventory_items"]
distribution_centers = db["distribution_centers"]

# Sample retrieval functions

def get_user_by_email(email):
    return users.find_one({"email": email})

def get_user_orders(user_id):
    return list(orders.find({"user_id": user_id}))

def get_order_items(order_id):
    return list(order_items.find({"order_id": order_id}))

def get_product_info(product_id):
    return products.find_one({"_id": product_id})

def get_inventory_by_product(product_id):
    return list(inventory_items.find({"product_id": product_id}))

def get_distribution_center(center_id):
    return distribution_centers.find_one({"_id": center_id})


# Test example
if __name__ == "__main__":
    # Change these values based on your data
    user = get_user_by_email("demo_user@example.com")
    if user:
        print("User:", user)
        user_orders = get_user_orders(user["_id"])
        print("Orders:", user_orders)
