from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..db.models import BookIn, BookOut
from ..crud import book_crud as crud
from ..db.database import get_session

router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=list[BookOut])
def read_all_books(author: str | None = None, session: Session = Depends(get_session)):
    return crud.read_all_books(session, author)


@router.get("/{book_id}", response_model=BookOut)
def read_book_by_id(book_id: int, session: Session = Depends(get_session)):
    return crud.read_book_by_id(session, book_id)


@router.post("", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def save_book(book_in: BookIn, session: Session = Depends(get_session)):
    return crud.save_book(session, book_in)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book_id: int, session: Session = Depends(get_session)):
    return crud.delete_book_by_id(session, book_id)
