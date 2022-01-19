from pymongo import *

mongo = MongoClient(
    "mongodb+srv://Bot-Lottery:zwrHE8Beki390MYs@bot-discord.ggepi.mongodb.net/LotteryBot?retryWrites=true&w=majority")

db = mongo.LotteryBot

coll = db.stockValue

docs = coll.find().sort("_id", ASCENDING)
for doc in docs:
    if "T" in doc["time"]:
        coll.update_one({"_id": doc["_id"]}, {"$set": {"time": doc["time"].replace("T", " ")}})
