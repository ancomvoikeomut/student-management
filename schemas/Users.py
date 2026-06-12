from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
class UserBase(BaseModel):
    username: str
    role : str
class UserCreate(UserBase):
    pass
class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes = True)
    id : int
    