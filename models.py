from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
class Users(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    username :Mapped[str] =  mapped_column(String, nullable = False)
    role:Mapped[str] = mapped_column(String, nullable = False)

class Teacher(Base):
    __tablename__ = "teacher"
    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    user_id:Mapped[int] = mapped_column(ForeignKey  ("users.id"))
    fullname:Mapped[str] =  mapped_column(String, nullable = False)
    phone:Mapped[str] = mapped_column(String, nullable =  False)
class Student(Base):
    __tablename__ = "students"
    id:Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    user_id: Mapped[int] = mapped_column(ForeignKey  ("users.id"))
    fullname:Mapped[str] =  mapped_column(String, nullable =  False)
    birth_data :Mapped[DateTime] =  mapped_column(DateTime, nullable = False)
    gender : Mapped[str] =  mapped_column(String, nullable = False)
    address: Mapped[str] = mapped_column(String, nullable = False)
    phone :Mapped[str] =  mapped_column(String, nullable = False)
    parent_name: Mapped[str]=  mapped_column(String, nullable  = False)

class Classes(Base):
    __tablename__ = "classes"
    id: Mapped[int] =  mapped_column(Integer, primary_key = True, index= True)
    name: Mapped[str] =  mapped_column(String, nullable = False)
    grades: Mapped[int] = mapped_column(Integer, nullable = False)
    homeroom_teacher_id : Mapped[int] = mapped_column(ForeignKey ("teacher.id"))
    school_year: Mapped[str] = mapped_column(String, nullable = False)
class Subject(Base):
    __tablename__ = "subject"
    id: Mapped[int] =  mapped_column(Integer,primary_key =  True, index= True)
    subject_name:Mapped[str] = mapped_column(String, nullable = False)
    credit: Mapped[int]  = mapped_column(Integer, nullable = False)
class Class_student(Base):
    __tablename__ = "class_student"
    id: Mapped[int] =  mapped_column(Integer, primary_key =  True, index= True)
    class_id : Mapped[int] = mapped_column(ForeignKey ("classes.id"))
    student_id : Mapped[int] = mapped_column(ForeignKey  ("students.id"))
    school_year: Mapped[str] = mapped_column( String, nullable = False)
class Attendances(Base):
    __tablename__ = "attendances"
    id: Mapped[int] = mapped_column(Integer, primary_key = True, index= True)
    student_id : Mapped[int] =  mapped_column(ForeignKey ( "students.id"))
    class_id : Mapped[int] =  mapped_column(ForeignKey  ("classes.id"))
    date: Mapped[DateTime] =  mapped_column(DateTime, nullable  = False)
    status : Mapped[String] = mapped_column(String, nullable = False)
class Grades(Base):
    __tablename__ = "grades"
    id:Mapped[int] =  mapped_column(Integer, primary_key =  True, index = True)
    student_id: Mapped[int] = mapped_column(ForeignKey  ("students.id"))
    subject_id : Mapped[int] = mapped_column(ForeignKey  ( "subject.id"))
    class_id : Mapped[int] = mapped_column(ForeignKey  ("classes.id"))
    oral_score : Mapped[float] = mapped_column(Float, nullable =  False)
    score_15min: Mapped[float] = mapped_column( Float, nullable = False)
    score_45min : Mapped[float] =  mapped_column(Float, nullable = False)
    final_score: Mapped[float] =  mapped_column( Float, nullable = False)
    average: Mapped[float] =  mapped_column(Float, nullable = False)
class Subject_Assignment(Base):
    __tablename__ = "subject_assignment"
    id : Mapped[int]  = mapped_column(Integer,primary_key = True, nullable = False)
    teacher_id: Mapped[int] =  mapped_column(ForeignKey  ( "teacher.id"))
    subject_id: Mapped[int] =  mapped_column(ForeignKey   ("subject.id"))
    class_id : Mapped[int] =  mapped_column(ForeignKey  ("classes.id"))
