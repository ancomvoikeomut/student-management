from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from database import get_db
import models
from schemas.Teachers import TeacherResponse , TeacherCreate
from fastapi import FastAPI, Request, HTTPException, status, Depends, APIRouter
from typing import Annotated 
router = APIRouter(prefix="/teachers", tags=["teachers"])  

@router.get("/", response_model = list[TeacherResponse])
async def get_teacher( users : TeacherCreate ,db: Annotated[AsyncSession, Depends(get_db)]):
    results = await db.execute(select(models.Teacher).where(models.Teacher.id ==  users))
    abc = results.scalars().all()
    return abc
@router.post("/", response_model =  TeacherResponse)
async def create_teacher(data :  TeacherCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    user_query = await db.execute(select(models.Users).where(models.Users.id == data.user_id))
    user_exists = user_query.scalars().first()
    if  user_exists:
        raise HTTPException(status_code=  status.HTTP_404_NOT_FOUND)
    new_teacher = models.Teacher(
        fullname  = data.fullname,
        phone = data.phone
    )
    db.add(new_teacher)
    await db.commit()
    await db.refresh(new_teacher)
@router.delete("/{user_id}", response_model = TeacherResponse)
async def deleteTeacher(user_id :  int , db: Annotated[AsyncSession, Depends(get_db)]):
    results  = await db.execute(select(models.Users).where(models.Users.id == user_id))
    abc = results.scalars().first()
    if not abc:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)
    await db.delete(abc)
    await db.commit()
    
        
