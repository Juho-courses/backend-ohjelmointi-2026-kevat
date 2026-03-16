from fastapi import APIRouter, status, Depends
from ..db.models import ShoeDb, ShoeIn
from ..crud import shoe_crud as crud
from sqlmodel import Session
from ..db.database import get_session

router = APIRouter(prefix="/shoes", tags=["shoes"])


@router.post("", response_model=ShoeDb, status_code=status.HTTP_201_CREATED)
def create_shoe(shoe_in: ShoeIn, session: Session = Depends(get_session)):
    return crud.create_shoe(session, shoe_in)


@router.get("", response_model=list[ShoeDb])
def get_shoes(manufacturer: str | None = None, session: Session = Depends(get_session)):
    return crud.get_shoes(session, manufacturer)


@router.get("/{shoe_id}", response_model=ShoeDb,
            responses={
                404: {"description": "shoe not found"}
            })
def get_shoe_by_id(shoe_id: int, session: Session = Depends(get_session)):
    return crud.get_shoe_by_id(session, shoe_id)


@router.delete("/{shoe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shoe(shoe_id: int, session: Session = Depends(get_session)):
    return crud.delete_shoe(session, shoe_id)
