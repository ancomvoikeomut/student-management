from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
class StudentBase(BaseModel):
    fullname: str = Field(min_length  = 1 , max_length = 20)
    birth_data:datetime 

    gender:str 
    address:str
    phone :str
    parent_name:str
class StudentCreate(StudentBase):
    user_id : int
class StudentResponse(StudentBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)
class StudentUpdate(StudentBase):
    phone :str|None = None
    address:str|None = None

    gender:str | None = None
    


