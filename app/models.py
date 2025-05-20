from typing import Optional
from sqlmodel import SQLModel, Field

class ItemBase(SQLModel):
    name: str
    description: Optional[str] = None
    price: float


class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: int

class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)