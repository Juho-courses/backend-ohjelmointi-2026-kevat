from fastapi import FastAPI
from .routers import book_router, author_router

app = FastAPI()

app.include_router(book_router.router)
app.include_router(author_router.router)
