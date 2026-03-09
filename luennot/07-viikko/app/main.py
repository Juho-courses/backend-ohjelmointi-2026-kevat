from fastapi import FastAPI, HTTPException, status
from sqlmodel import SQLModel
from .routers import manu_router, shoe_router

app = FastAPI()

app.include_router(manu_router.router)
app.include_router(shoe_router.router)
