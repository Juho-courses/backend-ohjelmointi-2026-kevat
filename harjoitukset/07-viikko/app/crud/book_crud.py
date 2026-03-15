from fastapi import HTTPException
from ..db.models import BookIn, BookOut


books = [
    {"id": 0, "title": "Book 1", "author": "Author 1"},
    {"id": 1, "title": "Book 2", "author": "Author 2"},
    {"id": 2, "title": "Book 3", "author": "Author 1"},
]


def read_all_books(author: str | None = None):
    if not author:
        return books
    return [b for b in books if b["author"] == author]


def read_book_by_id(book_id: int):
    bs = [b for b in books if b["id"] == book_id]
    if len(bs) == 0:
        raise HTTPException(
            status_code=404, detail=f"Book with id {book_id} not found")

    return bs[0]


def save_book(book_in: BookIn):
    new_id = len(books)
    book = BookOut(**book_in.model_dump(), id=new_id)
    books.append(book.model_dump())
    return book


def delete_book_by_id(book_id: int):
    bs = [b for b in books if b["id"] == book_id]
    if len(bs) == 0:
        raise HTTPException(
            status_code=404, detail=f"Book with id {book_id} not found")
    del books[book_id]
