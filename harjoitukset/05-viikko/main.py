from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 0, "title": "Book 1", "author": "Author 1"},
    {"id": 1, "title": "Book 2", "author": "Author 2"},
    {"id": 2, "title": "Book 3", "author": "Author 1"},
]


@app.get("/books")
def read_all_books(author: str | None = None):
    if not author:
        return books
    return [b for b in books if b["author"] == author]


@app.get("/books/{book_id}")
def read_book_by_id(book_id: int):
    return [b for b in books if b["id"] == book_id][0]
