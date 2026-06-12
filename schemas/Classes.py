from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
class ClassBase(BaseModel):
    name: str
    grades: int
    school_year: int
class ClassCreate(ClassBase):
    homeroom_teacher_id :int
class ClassResponse(ClassBase):
    model_config = ConfigDict(from_attributes=True)
    id : int
    homeroom_teacher_id :int

    