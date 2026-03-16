from fastapi import FastAPI
from pymongo import MongoClient

# ─── DATABASE CONNECTION ──────────────────────────
client = MongoClient("mongodb+srv://subbu:subbu@cluster0.obloh0f.mongodb.net/?appName=Cluster0")
db = client["ecommerce"]

# ─── COLLECTIONS ─────────────────────────────────
users_collection    = db["users"]
products_collection = db["products"]
orders_collection   = db["orders"]

# ─── APP ─────────────────────────────────────────
app = FastAPI()

# ─── ROOT ─────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "E-commerce API is running!"}

# ─── USERS ───────────────────────────────────────
@app.post("/users")
def create_user(user: dict):
    result = users_collection.insert_one(user)
    return {"message": "User created!", "id": str(result.inserted_id)}

@app.get("/users")
def get_users():
    users = []
    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

# ─── PRODUCTS ────────────────────────────────────
@app.post("/products")
def create_product(product: dict):
    result = products_collection.insert_one(product)
    return {"message": "Product created!", "id": str(result.inserted_id)}

@app.get("/products")
def get_products():
    products = []
    for product in products_collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products

# ─── ORDERS ──────────────────────────────────────
@app.post("/orders")
def create_order(order: dict):
    result = orders_collection.insert_one(order)
    return {"message": "Order created!", "id": str(result.inserted_id)}

@app.get("/orders")
def get_orders():
    orders = []
    for order in orders_collection.find():
        order["_id"] = str(order["_id"])
        orders.append(order)
    return orders

# ─── BULK INSERT ──────────────────────────────────
@app.post("/seed")
def seed_data():
    # 10 users
    users = [
        {"name": "Subbu",   "email": "subbu@gmail.com",   "age": 23},
        {"name": "Rahul",   "email": "rahul@gmail.com",   "age": 25},
        {"name": "Priya",   "email": "priya@gmail.com",   "age": 22},
        {"name": "Amit",    "email": "amit@gmail.com",    "age": 28},
        {"name": "Sneha",   "email": "sneha@gmail.com",   "age": 24},
        {"name": "Kiran",   "email": "kiran@gmail.com",   "age": 26},
        {"name": "Divya",   "email": "divya@gmail.com",   "age": 21},
        {"name": "Vikram",  "email": "vikram@gmail.com",  "age": 30},
        {"name": "Meera",   "email": "meera@gmail.com",   "age": 27},
        {"name": "Arjun",   "email": "arjun@gmail.com",   "age": 29},
    ]

    # 10 products
    products = [
        {"name": "Laptop",     "price": 999.99,  "category": "Electronics", "stock": 50},
        {"name": "Phone",      "price": 499.99,  "category": "Electronics", "stock": 100},
        {"name": "Headphones", "price": 99.99,   "category": "Electronics", "stock": 200},
        {"name": "T-Shirt",    "price": 19.99,   "category": "Clothing",    "stock": 500},
        {"name": "Jeans",      "price": 49.99,   "category": "Clothing",    "stock": 300},
        {"name": "Shoes",      "price": 79.99,   "category": "Footwear",    "stock": 150},
        {"name": "Watch",      "price": 199.99,  "category": "Accessories", "stock": 75},
        {"name": "Bag",        "price": 59.99,   "category": "Accessories", "stock": 120},
        {"name": "Book",       "price": 14.99,   "category": "Education",   "stock": 400},
        {"name": "Desk",       "price": 299.99,  "category": "Furniture",   "stock": 30},
    ]

    # 10 orders
    orders = [
        {"user": "Subbu",  "product": "Laptop",     "quantity": 1, "total_price": 999.99,  "status": "delivered"},
        {"user": "Rahul",  "product": "Phone",      "quantity": 2, "total_price": 999.98,  "status": "pending"},
        {"user": "Priya",  "product": "Headphones", "quantity": 1, "total_price": 99.99,   "status": "shipped"},
        {"user": "Amit",   "product": "T-Shirt",    "quantity": 3, "total_price": 59.97,   "status": "delivered"},
        {"user": "Sneha",  "product": "Jeans",      "quantity": 1, "total_price": 49.99,   "status": "pending"},
        {"user": "Kiran",  "product": "Shoes",      "quantity": 2, "total_price": 159.98,  "status": "shipped"},
        {"user": "Divya",  "product": "Watch",      "quantity": 1, "total_price": 199.99,  "status": "delivered"},
        {"user": "Vikram", "product": "Bag",        "quantity": 2, "total_price": 119.98,  "status": "pending"},
        {"user": "Meera",  "product": "Book",       "quantity": 4, "total_price": 59.96,   "status": "delivered"},
        {"user": "Arjun",  "product": "Desk",       "quantity": 1, "total_price": 299.99,  "status": "shipped"},
    ]

    users_collection.insert_many(users)
    products_collection.insert_many(products)
    orders_collection.insert_many(orders)

    return {
        "message": "Data seeded successfully!",
        "users": len(users),
        "products": len(products),
        "orders": len(orders)
    }