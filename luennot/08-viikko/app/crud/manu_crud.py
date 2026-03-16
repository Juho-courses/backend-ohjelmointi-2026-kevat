from ..db.models import ManufacturerIn, ManufacturerDb

manus = [
    {"id": 0, "name": "Hoka"},
    {"id": 1, "name": "Nike"}
]


def create_manufacturer(manu_in: ManufacturerIn):
    new_id = max([s["id"] for s in manus]) + 1
    manu = ManufacturerDb(id=new_id, **manu_in.model_dump())
    manus.append(manu.model_dump())
    return manu


def get_manufacturer():
    return manus
