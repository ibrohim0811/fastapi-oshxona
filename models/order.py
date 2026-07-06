from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Session

from database import Base

class StatusChoices(str, Enum):
    PENDING = "pending"
    PREPARING = "preparing"
    DELIVERY = "delivery"
    DELIVERED = "delivered"
    DECLINED = "declined"

class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    status: Mapped[StatusChoices] = mapped_column(default=StatusChoices.PENDING)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))


def orders(db: Session):
    return db.query(Order).all()


def order(order_id: int, db: Session):
    return db.query(Order).filter(Order.id == order_id).first()


def order_create(customer_id: int, db: Session):
    new_order = Order(
        customer_id=customer_id
    )
    db.add(new_order)
    db.commit()


def order_update(order_id: int, status: str, customer_id: int, db: Session):
    upd_order = db.query(Order).filter(Order.id == order_id).first()
    if upd_order:
        upd_order.status = status
        upd_order.customer_id = customer_id
        db.commit()
        db.refresh(upd_order)


def order_delete(order_id: int, db: Session):
    order_item = db.query(Order).filter(Order.id == order_id).first()
    if order_item:
        db.delete(order_item)
        db.commit()