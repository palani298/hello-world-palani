from sqlmodel import Session, select
from typing import List, Optional

from .models import Item, ItemCreate, ItemRead

def create_item(session: Session, item_data: dict) -> ItemRead:
    # Validate input data
    validated = ItemCreate.model_validate(item_data)
    db_item = Item.from_orm(validated)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    # Validate and return output data
    return ItemRead.model_validate(db_item)


def get_item(session: Session, item_id: int) -> Optional[ItemRead]:
    db_item = session.get(Item, item_id)
    if not db_item:
        return None
    return ItemRead.model_validate(db_item)


def list_items(session: Session) -> List[ItemRead]:
    items = session.exec(select(Item)).all()
    return [ItemRead.model_validate(item) for item in items]


def update_item(session: Session, item_id: int, item_data: dict) -> Optional[ItemRead]:
    db_item = session.get(Item, item_id)
    if not db_item:
        return None
    # Validate update payload
    validated = ItemCreate.model_validate(item_data)
    for key, value in validated.model_dump().items():
        setattr(db_item, key, value)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return ItemRead.model_validate(db_item)


def delete_item(session: Session, item_id: int) -> bool:
    db_item = session.get(Item, item_id)
    if not db_item:
        return False
    session.delete(db_item)
    session.commit()
    return True
