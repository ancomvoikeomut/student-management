from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
class SubjectBase(BaseModel):
    credit : str
    subject_name : str
class SubjectCreate(SubjectBase):
    pass
class SubjectResponse(SubjectBase):
    model_config = ConfigDict(from_attributes=True)
    id : int
    