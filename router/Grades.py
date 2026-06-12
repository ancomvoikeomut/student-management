from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from database import get_db
import models
from schemas.Grades import GradesResponse, GradesCreate
from fastapi import FastAPI, Request, HTTPException, status, Depends, APIRouter
from typing import Annotated 
router = APIRouter(prefix="/grades", tags=["grandes"])  
@router.get("/", response_model = list[GradesResponse])
async def get_grades(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Grades))
    abc= result.scalars().all()
    return abc
@router.post("/", response_model =  GradesResponse)
async def create_grades(data:GradesCreate, db: Annotated[AsyncSession, Depends(get_db)] ):
    results = await db.execute(select(models.Grades).where(models.Grades.student_id ==  data.student_id))
    abc = results.scalars().first()
    if not abc:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    new_grades = models.Grades(
        oral_score = data.oral_score,
        score_15min = data.score_15min,
        score_45min = data.score_45min,
        final_score = data.final_score,
        average = data.average
    )
    db.add(new_grades)
    await db.commit()
    await db.refresh(new_grades)
@router.delete("{grades_id}",status_code =  status.HTTP_204_NO_CONTENT)
async def  delete_grades(grades_id : int, db: Annotated[AsyncSession, Depends(get_db)]):
    results = await db.execute(select(models.Grades).where(models.Grades.id == grades_id))
    abc = results.scalars().first()
    if not abc:
        raise HTTPException(status_code=  status.HTTP_404_NOT_FOUND)
    await db.delete(abc)
    await db.commit()