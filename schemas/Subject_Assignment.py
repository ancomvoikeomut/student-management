from pydantic import BaseModel, ConfigDict

# ==========================================
# SUBJECT ASSIGNMENT SCHEMAS
# ==========================================

class SubjectAssignmentBase(BaseModel):
    # Vì bảng này không có thuộc tính text thuần túy nào (như note, school_year...)
    # nên chúng ta có thể để pass hoặc bỏ qua lớp Base này.
    pass


class SubjectAssignmentCreate(BaseModel):
    # Lúc tạo phân công, bắt buộc phải truyền vào "Bộ ba" Khóa ngoại này
    teacher_id: int
    subject_id: int
    class_id: int


class SubjectAssignmentResponse(SubjectAssignmentCreate):
    # Kế thừa lại bộ ba ID ở trên, và THÊM Khóa chính id hệ thống tự đẻ
    id: int

    # Cấu hình để Pydantic hiểu và đọc được dữ liệu từ Object của SQLAlchemy
    model_config = ConfigDict(from_attributes=True)