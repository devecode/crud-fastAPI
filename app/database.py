from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os
load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.prosperia

user_collection = database.get_collection("users")
