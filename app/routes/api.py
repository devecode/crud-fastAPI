from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from ..users.user_crud import add_user, retrieve_users, retrieve_user, update_user, delete_user
from ..users.models import User, UserRead
from ..movie.movie_crud import add_movie, retrieve_movies, retrieve_movie, update_movie, delete_movie, retrieve_movies_by_user
from ..movie.models import Movie, MovieRead 

router = APIRouter()

tags = ["Users"]

@router.post("/users/", response_description="Add new user", description="Creates a new user in the system.", response_model=User, tags=tags)
async def create_user(user: User = Body(...)):
  user = jsonable_encoder(user)
  new_user = await add_user(user)
  return new_user

@router.get("/users/", response_description="Users retrieved", response_model=List[UserRead], tags=tags)
async def get_users():
  users = await retrieve_users()
  if users:
    return users
  raise HTTPException(status_code=404, detail="Users not found")

@router.get("/users/{user_id}", response_description="User retrieved", response_model=UserRead, tags=tags)
async def get_user(user_id: str):
  try:
    user = await retrieve_user(user_id)
    if user:
      return user
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
  except ValueError as e:
      raise HTTPException(status_code=400, detail=str(e))

@router.put("/users/{id}", response_description="User data updated", tags=tags)
async def update_user_data(id: str, req: User = Body(...)):
  updated_user = await update_user(id, req.dict(exclude_unset=True))
  if updated_user:
    return {"message": "User updated successfully."}
  raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{id}", response_description="User deleted", tags=tags)
async def delete_user_data(id: str):
  deleted_user = await delete_user(id)
  if deleted_user:
    return {"message": "User deleted successfully."}
  raise HTTPException(status_code=404, detail="User not found")

@router.post("/movies/", response_description="Add new movie", description="Creates a new movie in the system.", response_model=Movie, tags=["Movies"])
async def create_movie(movie: Movie = Body(..., embed=True)):
    movie_dict = movie.dict()
    new_movie = await add_movie(movie_dict)
    return new_movie

@router.get("/movies/", response_description="Movies retrieved", response_model=List[MovieRead], tags=["Movies"])
async def get_movies():
    movies = await retrieve_movies()
    if movies:
        return movies
    raise HTTPException(status_code=404, detail="Movies not found")

@router.get("/movies/{movie_id}", response_description="Movie retrieved", response_model=MovieRead, tags=["Movies"])
async def get_movie(movie_id: str):
    try:
        movie = await retrieve_movie(movie_id)
        if movie:
            return movie
        raise HTTPException(status_code=404, detail=f"Movie with ID {movie_id} not found")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{user_id}/movies", response_description="Movies retrieved by user ID", response_model=List[MovieRead], tags=["Movies"])
async def get_movies_by_user(user_id: str):
    try:
        movies = await retrieve_movies_by_user(user_id)
        if movies:
            return movies
        raise HTTPException(status_code=404, detail=f"No movies found for user with ID {user_id}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
