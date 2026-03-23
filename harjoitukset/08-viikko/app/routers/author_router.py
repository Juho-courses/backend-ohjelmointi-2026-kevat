from fastapi import APIRouter, status, Depends
from ..db.models import AuthorIn, AuthorDb
from ..crud import author_crud as crud
from ..db.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("", response_model=list[AuthorDb])
def read_all_authors(name: str | None = None, session: Session = Depends(get_session)):
    return crud.read_all_authors(session, name)


@router.get("/{author_id}", response_model=AuthorDb)
def read_author_by_id(author_id: int, session: Session = Depends(get_session)):
    return crud.read_author_by_id(session, author_id)


@router.post("", response_model=AuthorDb, status_code=status.HTTP_201_CREATED)
def save_author(author_in: AuthorIn, session: Session = Depends(get_session)):
    return crud.save_author(session, author_in)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_by_id(author_id: int, session: Session = Depends(get_session)):
    return crud.delete_author_by_id(session, author_id)
