from fastapi import HTTPException
from sqlmodel import Session, select
from ..db.models import AuthorDb, AuthorIn


def read_all_authors(session: Session, name: str | None = None):
    if not name:
        return session.exec(select(AuthorDb)).all()
    return session.exec(select(AuthorDb).where(AuthorDb.name == name)).all()


def read_author_by_id(session: Session, author_id: int):
    author = session.get(AuthorDb, author_id)
    if not author:
        raise HTTPException(
            status_code=404, detail=f"Author with id {author_id} not found")

    return author


def save_author(session: Session, author_in: AuthorIn):
    author = AuthorDb.model_validate(author_in)
    session.add(author)
    session.commit()
    session.refresh(author)
    return author


def delete_author_by_id(session: Session, author_id: int):
    author = session.get(AuthorDb, author_id)
    if not author:
        raise HTTPException(
            status_code=404, detail=f"Author with id {author_id} not found")

    session.delete(author)
    session.commit()
