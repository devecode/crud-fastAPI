from pydantic import BaseModel, Field, EmailStr, validator
import re
from datetime import datetime
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    fullname: str = Field(..., description="The full name of the user.")
    age: int = Field(..., gt=0, description="The age of the user. Must be greater than 0.")
    phone_number: str = Field(..., description="The phone number of the user.")
    email: EmailStr = Field(..., description="The email address of the user.")
    createdAt: datetime = Field(default_factory=datetime.utcnow, description="The timestamp when the user was created. Automatically set to the current UTC time.")

    @validator('age')
    def age_must_be_number(cls, value):
      if not isinstance(value, int):
        raise ValueError('Age must be a number')
      return value

    @validator('phone_number')
    def validate_phone_number(cls, v):
      pattern = re.compile(r"^\+\d{1,3}\d{10}$")
      if not pattern.match(v):
        raise ValueError('Phone number must include country code followed by 10 digits')
      return v

    class Config:
      allow_population_by_field_name = True
      json_encoders = {ObjectId: lambda o: str(o)}
      schema_extra = {
        "example": {
          "fullname": "Ing. Ricardo Saucedo",
          "age": 30,
          "phone_number": "+524171270033",
          "email": "user@example.com",
          "createdAt": "2024-03-11T00:00:00"
        }
      }

class UserRead(User):
    id: Optional[str] = Field(None, alias='id')

    class Config:
      allow_population_by_field_name = True
      arbitrary_types_allowed = True
      json_encoders = {ObjectId: str}
      orm_mode = True
