from fastapi import FastAPI
from .routers import manu_router, shoe_router
from .db.database import create_db_and_tables
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield create_db_and_tables()

app = FastAPI(lifespan=lifespan)

app.include_router(manu_router.router)
app.include_router(shoe_router.router)
