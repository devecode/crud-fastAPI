from app.database import user_collection
from bson import ObjectId
from datetime import datetime

def user_helper(user: dict) -> dict:
    prepared_user = {
        "id": str(user["_id"]),
        **{k: v for k, v in user.items() if k != "_id"},
    }
    return prepared_user


async def add_user(user_data: dict) -> dict:
    user_data["createdAt"] = datetime.utcnow()
    result = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": result.inserted_id})
    return user_helper(new_user)

async def retrieve_users():
    users = await user_collection.find().to_list(length=None)
    prepared_users = [user_helper(user) for user in users]
    return prepared_users

async def retrieve_user(user_id: str) -> dict:
    if not ObjectId.is_valid(user_id):
        return ValueError("Invalid ID format")
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)
    return None


async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    result = await user_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    if result.modified_count:
        return True
    return False

async def delete_user(id: str):
    result = await user_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return True
    return False
