from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
class TeacherBase(BaseModel):
    fullname: str
    phone: str
class TeacherCreate(TeacherBase):
    user_id : int
class TeacherResponse(TeacherBase):
    id : int
    user_id : int
    model_config = ConfigDict(from_attributes=True)
class TeacherUpdate(TeacherBase):
    fullname : str|None
    phone : str| None