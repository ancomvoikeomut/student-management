from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
class AttendancesBase(BaseModel):
    status : str
    date : datetime
class Attendances_Create(AttendancesBase):
    classes_id : int
    student_id : int
class AttendancesResponse(AttendancesBase):
    id : int 
    classes_id : int
    model_config = ConfigDict(from_attributes=True)
    student_id : int