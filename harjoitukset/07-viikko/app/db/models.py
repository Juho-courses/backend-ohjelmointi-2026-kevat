from sqlmodel import SQLModel


class AuthorBase(SQLModel):
    name: str


class AuthorIn(AuthorBase):
    pass


class AuthorDb(AuthorBase):
    id: int


class BookBase(SQLModel):
    title: str
    author: str


class BookIn(BookBase):
    pass


class BookOut(BookBase):
    id: int
