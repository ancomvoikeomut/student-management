from pydantic import BaseModel, ConfigDict, Field, EmailStr
class Class_student(BaseModel):
    school_year: str
class Class_student_Create(Class_student):
    class_id : int
    teacher_id : int
class Class_Student_Response(Class_student):
    model_config = ConfigDict(from_attributes=True)
    id : int
    class_id : int
    teacher_id : int