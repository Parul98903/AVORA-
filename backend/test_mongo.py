from pymongo import MongoClient

uri = "mongodb+srv://The Style Algorithmadmin:FitMatch@The Style Algorithm-cluster.ux5f8vo.mongodb.net/The Style Algorithm?retryWrites=true&w=majority&appName=The Style Algorithm-cluster"

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed:")
    print(e)