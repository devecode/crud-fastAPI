from app.database import movie_collection
from bson import ObjectId
from datetime import datetime

def movie_helper(movie: dict) -> dict:
    if 'user_id' in movie and isinstance(movie['user_id'], ObjectId):
        movie['user_id'] = str(movie['user_id'])

    prepared_movie = {
        "id": str(movie["_id"]),
        **{k: v for k, v in movie.items() if k != "_id"},
    }
    return prepared_movie


async def add_movie(movie_data: dict) -> dict:
    movie_data["createdAt"] = datetime.utcnow()
    result = await movie_collection.insert_one(movie_data)
    new_movie = await movie_collection.find_one({"_id": result.inserted_id})
    return movie_helper(new_movie)

async def retrieve_movies():
    movies = await movie_collection.find().to_list(length=None)
    return [movie_helper(movie) for movie in movies]

async def retrieve_movie(movie_id: str) -> dict:
    if not ObjectId.is_valid(movie_id):
        return ValueError("Invalid ID format")
    movie = await movie_collection.find_one({"_id": ObjectId(movie_id)})
    if movie:
        return movie_helper(movie)
    return None

async def retrieve_movies_by_user(user_id: str):
    movies = await movie_collection.find({"user_id": ObjectId(user_id)}).to_list(length=None)
    if movies:
        return [movie_helper(movie) for movie in movies]
    else:
        return None


async def update_movie(id: str, data: dict):
    if len(data) < 1:
        return False
    result = await movie_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    if result.modified_count:
        return True
    return False

async def delete_movie(id: str):
    result = await movie_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return True
    return False
