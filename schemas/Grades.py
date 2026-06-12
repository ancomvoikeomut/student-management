from pydantic import BaseModel, ConfigDict, Field, EmailStr
class GradesBase(BaseModel):
    oral_score : float
    score_15min: float
    score_45min : float
    final_score: float
    average:float
class GradesResponse(GradesBase):
    model_config = ConfigDict(from_attributes=True)
    id : int 
    subject_id : int
    class_id : int
    student_id : int

class GradesCreate(GradesBase):
    subject_id : int
    class_id : int
    student_id : int
