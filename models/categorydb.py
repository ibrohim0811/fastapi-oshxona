from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Session
from database import Base



class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))


def categories(db: Session):
    return db.query(Category).all()


def category_detail(id, db: Session):
    return db.query(Category).filter(id == id).first()


def category_create(category_name: str, db: Session):
    category = Category(
        name=category_name
    )
    db.add(category)
    db.commit()
    


def category_update(id: int, category_name: str, db: Session):
    category = db.query(Category).filter(Category.id == id).first()
    if category:
        category.name = category_name
        db.commit()
        db.refresh(category)
    return category


def category_delete(id: int, db: Session):
    category = db.query(Category).filter(Category.id == id).first()
    if category:
        db.delete(category)
        db.commit()
    return category


