from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from database import get_db
import models
from schemas.Students import StudentCreate, StudentResponse
from fastapi import FastAPI, Request, HTTPException, status, Depends, APIRouter
from typing import Annotated 
router = APIRouter(prefix="/students", tags=["students"])  
@router.get("/", response_model = list[StudentResponse])
async def get_student(db:Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Student))
    abc = result.scalars().first()
    return abc
@router.post("/", response_model =  StudentResponse)
async def createStudent(data: StudentCreate, db:Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Student))
    abc = result.scalars().first()
    if abc:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)
    new_student = models.Student(
    fullname =  data.fullname,
    birth_data = data.birth_data,
    gender = data.gender,
    address = data.address,

    phone = data.phone,
    parent_name = data.parent_name)
    db.add(new_student)
    await db.commit()
@router.delete("/{student_id}, response_model = StudentResponse")
async def delete_student (student_id:int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Student).where(models.Student.id == student_id))
    abc= result.scalars().first()
    if not abc:
        raise HTTPException(status_code=  status.HTTP_404_NOT_FOUND)
    await db.delete(abc)
    await db.commit()