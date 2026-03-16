from fastapi import HTTPException, status
from ..db.models import ShoeDb, ShoeIn
from sqlmodel import Session, select


def create_shoe(session: Session, shoe_in: ShoeIn):
    shoe = ShoeDb.model_validate(shoe_in)
    session.add(shoe)
    session.commit()
    session.refresh(shoe)
    return shoe


def get_shoes(session: Session, manufacturer: str | None = None):
    if manufacturer:
        statement = select(ShoeDb).where(ShoeDb.manufacturer == manufacturer)
        return session.exec(statement).all()
    return session.exec(select(ShoeDb)).all()


def get_shoe_by_id(session: Session, shoe_id: int):
    # stmt = select(ShoeDb).where(ShoeDb.id == shoe_id)
    # return session.exec(stmt).first()
    shoe = session.get(ShoeDb, shoe_id)
    if not shoe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="shoe not found")
    return shoe


def delete_shoe(session: Session, shoe_id: int):
    shoe = session.get(ShoeDb, shoe_id)
    if not shoe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="shoe not found")

    session.delete(shoe)
    session.commit()
