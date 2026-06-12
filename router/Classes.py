from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from database import get_db
import models
from schemas.Classes import ClassResponse, ClassCreate
from fastapi import FastAPI, Request, HTTPException, status, Depends, APIRouter
from typing import Annotated 
router = APIRouter(prefix="/classes", tags=["classes"])  
@router.get("/", response_model = list[ClassResponse])
async def get_teacher(db: Annotated[AsyncSession, Depends(get_db)]):
    results = await  db.execute(select(models.Classes))
    abc = results.scalars().all()
    return abc
@router.post("/", response_model =  ClassResponse)
async def createClass(data:ClassCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await  db.execute(select(models.Classes).where(models.Classes.name == data.name))
    abc = result.scalars().first()
    if abc:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)
    new_class = models.Classes(
        name = data.name,
        grades = data.grades,
        school_year =  data.school_year,
    

    )
    db.add(new_class)
    await db.commit()
    await db.refresh(new_class)
@router.delete("{classes_id}", status_code = status.HTTP_204_NO_CONTENT)
async def deleteClass(classes_id:int, db: Annotated[AsyncSession, Depends(get_db)]):
    results = await db.execute(select(models.Classes).where(models.Classes.id == classes_id))
    abc = results.scalars().first()
    if not abc : 
           raise HTTPException(status_code=  status.HTTP_404_NOT_FOUND)
    await db.delete(abc)
    await db.commit()
    await db.refresh(abc)

