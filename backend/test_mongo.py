from pymongo import MongoClient

uri = "mongodb+srv://avoraadmin:FitMatch@avora-cluster.ux5f8vo.mongodb.net/avora?retryWrites=true&w=majority&appName=avora-cluster"

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed:")
    print(e)