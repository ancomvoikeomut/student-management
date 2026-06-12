from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from router import Users
from starlette.exceptions import HTTPException as StarletteHTTPException
from schemas import Students,Teachers, Users,Grades,Subject,Subject_Assignment,Attendances,Class_student, Classes
from typing import Annotated 
from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
import models
from database import Base, engine , get_db
from router.Classes import router as classes_router
from router.Grades import router as grades_router
from router.Users import router as users_router
from router.Teachers import router as teachers_router

from contextlib import asynccontextmanager
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,

)
@asynccontextmanager
async def lifespan(_app: FastAPI):
    #startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()


app = FastAPI(lifespan = lifespan)
app.include_router(classes_router)
app.include_router(grades_router)
app.include_router(users_router)
app.include_router(teachers_router)
