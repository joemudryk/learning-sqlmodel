from typing import Optional

from sqlmodel import SQLModel, Field


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None
    gender: str


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
