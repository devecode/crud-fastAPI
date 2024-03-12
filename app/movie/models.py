from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class Movie(BaseModel):
    name: str = Field(..., description="The name of the movie.")
    description: str = Field(..., description="The description of the movie.")
    review: str = Field(..., description="The review of the movie.")
    createdAt: datetime = Field(default_factory=datetime.utcnow, description="The timestamp when the movie was created. Automatically set to the current UTC time.")
    rating: float = Field(..., gt=0, lt=6, description="The rating of the movie. Must be between 1 and 5.")
    user_id: str = Field(..., description="The ID of the user who added the movie.")

    class Config:
        json_encoders = {ObjectId: lambda o: str(o)}
        schema_extra = {
            "example": {
                "name": "Inception",
                "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                "review": "Mind-bending and innovative, a masterpiece of modern cinema.",
                "createdAt": "2024-04-05T00:00:00",
                "rating": 5,
                "user_id": "someuserid12345"
            }
        }

class MovieRead(Movie):
    id: Optional[str] = Field(None, alias='_id', description="The unique identifier of the movie.")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: lambda o: str(o)}
        orm_mode = True
