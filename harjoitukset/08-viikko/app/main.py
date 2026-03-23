from fastapi import FastAPI
from .routers import book_router, author_router
from .db.database import create_db_and_tables
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(book_router.router)
app.include_router(author_router.router)
