from fastapi import HTTPException
from ..db.models import AuthorDb, AuthorIn


authors = [
    {"id": 0, "name": "Author 1"},
    {"id": 1, "name": "Author 2"},
    {"id": 2, "name": "Author 3"},
]


def read_all_authors(name: str | None = None):
    if not name:
        return authors
    return [b for b in authors if b["name"] == name]


def read_author_by_id(author_id: int):
    aus = [b for b in authors if b["id"] == author_id]
    if len(aus) == 0:
        raise HTTPException(
            status_code=404, detail=f"Author with id {author_id} not found")

    return aus[0]


def save_author(author_in: AuthorIn):
    new_id = len(authors)
    author = AuthorDb(**author_in.model_dump(), id=new_id)
    authors.append(author.model_dump())
    return author


def delete_author_by_id(author_id: int):
    aus = [b for b in authors if b["id"] == author_id]
    if len(aus) == 0:
        raise HTTPException(
            status_code=404, detail=f"Author with id {author_id} not found")
    del authors[author_id]
