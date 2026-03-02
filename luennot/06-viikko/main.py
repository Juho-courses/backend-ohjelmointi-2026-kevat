from fastapi import FastAPI, HTTPException, status
from sqlmodel import SQLModel

app = FastAPI()

shoes = [
    {"id": 0, "model": "Speedgoat 5", "manufacturer": "Hoka"},
    {"id": 1, "model": "Air Zoom", "manufacturer": "Nike"},
    {"id": 2, "model": "Speedgoat 4", "manufacturer": "Hoka"},
]


class ShoeBase(SQLModel):
    model: str
    manufacturer: str


class ShoeDb(ShoeBase):
    id: int


class ShoeIn(ShoeBase):
    pass


@app.post("/shoes", response_model=ShoeDb, status_code=status.HTTP_201_CREATED)
def create_shoe(shoe_in: ShoeIn):
    new_id = max([s["id"] for s in shoes]) + 1
    shoe = ShoeDb(id=new_id, **shoe_in.model_dump())
    shoes.append(shoe.model_dump())
    return shoe


@app.get("/shoes", response_model=list[ShoeDb])
def get_shoes(manufacturer: str | None = None):
    if manufacturer:
        return [s for s in shoes if s["manufacturer"].lower() == manufacturer.lower()]
    return shoes


@app.get("/shoes/{shoe_id}", response_model=ShoeDb,
         responses={
             404: {"description": "shoe not found"}
         })
def get_shoe_by_id(shoe_id: int):
    shoe_list = [s for s in shoes if s["id"] == shoe_id]
    if len(shoe_list) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="shoe not found")
    return shoe_list[0]


@app.delete("/shoes/{shoe_id}", status_code=status.HTTP_204_NO_CONTENT)
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
