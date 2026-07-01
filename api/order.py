from fastapi import APIRouter, status, HTTPException
from typing import List

from crud.order import order, orders, order_update, order_create, order_delete
from schemas.orders import OrderSchema, OrderCreateSchema, OrderSchemaPatch, OrderSchemaid

router = APIRouter(
    tags=['order']
)


@router.get('/orders', response_model=List[OrderSchemaid])
def get_order():
    data = orders()
    if data is not None:
        formatted_data = [{"id": row[0], "name": row[1], "about": row[2], "price": row[3], "is_active": row[4], "category_id": row[5]} for row in data]
        return formatted_data
    raise HTTPException(404, "Baza bo'm-bo'sh")


@router.get('/order/{order_id}', response_model=List[OrderSchemaid])
def get_item(order_id: int):
    data = order(order_id=order_id)
    if data is not None:
        formatted_data = [{"id": data[0], "status": data[1], "customer_id": data[2]}]
        return formatted_data
    raise HTTPException(404, "Buyurtma mavjud emas!")


@router.post('/order/')
def create_item(order: OrderCreateSchema):
    order_create(status=order.status, customer_id=order.customer_id)   
    return {"message": "Yaratildi !", "status":status.HTTP_201_CREATED}


@router.put('/order/{order_id}')
def put_item(order_id: int, order: OrderSchema):
    order_update(
        order_id=order_id,
        status=order.status,
        customer_id=order.customer_id
    )
    return {"message":"Yangilandi!", "status":status.HTTP_200_OK}


@router.patch('/order/{order_id}')
def put_item(order_id: int, order: OrderSchemaPatch):
    order_update(
        order_id=order_id,
        status=order.status,
        customer_id=order.customer_id
    )
    return {"message":"Yangilandi!", "status":status.HTTP_200_OK}


@router.delete('/order/{order_id}')
def patch_item(order_id: int):
    if order(order_id):
        order_delete(order_id)
        return {"message":"O'chirildi!", "status":status.HTTP_204_NO_CONTENT}
    raise HTTPException(404, "Kiritilgan buyurtma topilmadi!")