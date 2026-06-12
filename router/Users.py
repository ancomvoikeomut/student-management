from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from database import get_db
import models
from schemas.Users import UserResponse , UserCreate
from fastapi import FastAPI, Request, HTTPException, status, Depends, APIRouter
from typing import Annotated 


router = APIRouter(prefix="/users", tags=["users"])  

@router.get("/", response_model=List[UserResponse])  
async def get_all(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Users))   
    users = result.scalars().all()
    return users
@router.post("/", response_model = UserResponse)
async def createUsers(users: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    results = await db.execute(select(models.Users).where(models.Users.username ==  users.username))
    exis_users = results.scalars().first()
    if exis_users:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUESR)
    new_users = models.Users(
        username =  users.username,
        role = users.role

    )
    db.add(new_users)
    await db.commit()
    await db.refresh(new_users)
@router.delete("/{users_id}", status_code =  status.HTTP_204_NO_CONTENT )
async def deleteusers(users_id : int, db: Annotated[AsyncSession, Depends(get_db)]):
    results = await db.execute(select(models.Users).where(models.Users.id == users_id))
    abc = results.scalars().first()
    if not abc:
        raise HTTPException(status_code=  status.HTTP_404_NOT_FOUND)
    await db.delete(abc)
    await db.commit()
