from fastapi import APIRouter, status
from ..db.models import ManufacturerDb, ManufacturerIn
from ..crud import manu_crud as crud

router = APIRouter(prefix="/manufacturers", tags=["manufacturers"])


@router.post("", response_model=ManufacturerDb, status_code=status.HTTP_201_CREATED)
def create_manufacturer(manu_in: ManufacturerIn):
    return crud.create_manufacturer(manu_in)


@router.get("", response_model=list[ManufacturerDb])
def get_manufacturer():
    return crud.get_manufacturer()
