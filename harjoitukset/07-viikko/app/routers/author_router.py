from fastapi import APIRouter, status
from ..db.models import AuthorIn, AuthorDb
from ..crud import author_crud as crud

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("", response_model=list[AuthorDb])
def read_all_authors(name: str | None = None):
    return crud.read_all_authors(name)


@router.get("/{author_id}", response_model=AuthorDb)
def read_author_by_id(author_id: int):
    return crud.read_author_by_id(author_id)


@router.post("", response_model=AuthorDb, status_code=status.HTTP_201_CREATED)
def save_author(author_in: AuthorIn):
    return crud.save_author(author_in)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_by_id(author_id: int):
    return crud.delete_author_by_id(author_id)
