from sqlmodel import SQLModel, Field


class AuthorBase(SQLModel):
    name: str


class AuthorIn(AuthorBase):
    pass


class AuthorDb(AuthorBase, table=True):
    id: int = Field(default=None, primary_key=True)


class BookBase(SQLModel):
    title: str
    author: str


class BookIn(BookBase):
    pass


class BookOut(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)
