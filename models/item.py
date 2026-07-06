from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Session
from database import Base


class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200))
    about: Mapped[str] = mapped_column(String(500))
    price: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
        

def items(db: Session):
    return db.query(Item).all()


def item(id: int, db: Session):
    item_ = db.query(Item).filter(Item.id == id).first()
    return item_


def item_create(name: str, about: str, price: int, category_id: int, db: Session):
    new_item = Item(
        name=name,
        about=about,
        price=price,
        category_id=category_id
    )
    db.add(new_item)
    db.commit()


def item_update(item_id: int, name: str, about: str, is_active: bool, price: int, category_id: int, db: Session):
    item_check = db.query(Item).filter(Item.id == item_id).first()
    if item_check:
        
        item_check.name=name,
        item_check.about=about,
        item_check.is_active=is_active,
        item_check.price=price,
        item_check.category_id=category_id
    
        db.commit()
        db.refresh(item_check)


def item_delete(item_id: int, db: Session):
    item_ = db.query(Item).filter(Item.id == item_id).first()
    if item_:   
        db.delete(item_)
        db.commit()
