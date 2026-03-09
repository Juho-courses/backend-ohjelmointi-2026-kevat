from sqlmodel import SQLModel


class ManufacturerBase(SQLModel):
    name: str


class ManufacturerIn(ManufacturerBase):
    pass


class ManufacturerDb(ManufacturerBase):
    id: int


class ShoeBase(SQLModel):
    model: str
    manufacturer: str


class ShoeDb(ShoeBase):
    id: int


class ShoeIn(ShoeBase):
    pass
