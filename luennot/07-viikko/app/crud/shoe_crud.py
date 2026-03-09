from fastapi import HTTPException, status
from ..db.models import ShoeDb, ShoeIn

shoes = [
    {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
]


def create_shoe(shoe_in: ShoeIn):
    new_id = max([s["id"] for s in shoes]) + 1
    shoe = ShoeDb(id=new_id, **shoe_in.model_dump())
    shoes.append(shoe.model_dump())
    return shoe


def get_shoes(manufacturer: str | None = None):
    if manufacturer:
        return [s for s in shoes if s["manufacturer"].lower() == manufacturer.lower()]
    return shoes


def get_shoe_by_id(shoe_id: int):
    shoe_list = [s for s in shoes if s["id"] == shoe_id]
    if len(shoe_list) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="shoe not found")
    return shoe_list[0]


def delete_shoe(shoe_id: int):
    index = None
    for i, s in enumerate(shoes):
        if s["id"] == shoe_id:
            index = i
            break
    if not index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="shoe not found")
    del shoes[index]
