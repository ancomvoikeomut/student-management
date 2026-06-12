from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from database import get_db
import models
from schemas.Subject import SubjectCreate, SubjectResponse
from fastapi import FastAPI, Request, HTTPException, status, Depends, APIRouter
from typing import Annotated 
router = APIRouter(prefix="/subjects", tags=["subjects"])  
@router.get("/", response_model = list[SubjectResponse])
async def get_subject(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Subject))
    abc = result.scalars().first()
    return abc
@router.post("/", response_model = SubjectResponse)
async def create_subject(data: SubjectCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Subject).where(models.Subject.subject_name == data.subject_name))
    abc = result.scalars().first()
    if abc:
        raise HTTPException(status_code= status.HTTP_404_)
    new_data = models.Student(
        subject_name = data.subject_name,
        credit = data.credit
    )
    db.add(new_data)
    await db.commit()
    await db.refresh(new_data)
@router.delete("/{subject_id}", response_model = SubjectResponse )
async def delete_subject(subject_id : int, db:Annotated[AsyncSession, Depends(get_db)]):
    results =  await db.execute(select(models.Subject).where(models.Subject.id == subject_id))
    abc = results.scalars().first()
    if not abc:
        raise HTTPException(status_code=  status.HTTP_404_NOT_FOUND)
    await db.delete(abc)
    await db.commit()

                               