from fastapi import HTTPException
from sqlmodel import Session, select
from ..db.models import BookIn, BookOut


def read_all_books(session: Session, author: str | None = None):
    if not author:
        return session.exec(select(BookOut)).all()

    statement = select(BookOut).where(BookOut.author == author)
    return session.exec(statement).all()


def read_book_by_id(session: Session, book_id: int):
    book = session.get(BookOut, book_id)
    print(book)
    if not book:
        raise HTTPException(
            status_code=404, detail=f"Book with id {book_id} not found")

    return book


def save_book(session: Session, book_in: BookIn):
    book = BookOut.model_validate(book_in)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def delete_book_by_id(session: Session, book_id: int):
    book = session.get(BookOut, book_id)
    if not book:
        raise HTTPException(
            status_code=404, detail=f"Book with id {book_id} not found")

    session.delete(book)
    session.commit()
