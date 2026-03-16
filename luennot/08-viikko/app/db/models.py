from sqlmodel import SQLModel, Field


class ManufacturerBase(SQLModel):
    name: str


class ManufacturerIn(ManufacturerBase):
    pass


class ManufacturerDb(ManufacturerBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ShoeBase(SQLModel):
    model: str
    manufacturer: str


class ShoeDb(ShoeBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ShoeIn(ShoeBase):
    pass
