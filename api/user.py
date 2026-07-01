from fastapi import APIRouter, HTTPException, status
from typing import List

from crud.user import (
customer, customers, 
customer_update, customer_create, 
customer_delete
)
from schemas.customer import CustomerSchema, CustomerSchemaPatch, CustomerChemaid

router = APIRouter(
    tags=['customer']
)

@router.get('/customers/', response_model=List[CustomerChemaid])
def get_customers():
    data = customers()

    formatted_data = [{"id":row[0], "first_name":row[1], "last_name":row[2], "email":row[3]} for row in data]
    return formatted_data


@router.get('/customer/{customer_id}')
def get_customer(customer_id: int):
    data = customer(customer_id=customer_id)
    if data:
        formatted_data = [{"id":data[0], "first_name":data[1], "last_name":data[2], "email":data[3]}]
        return formatted_data
    raise HTTPException(404, "Bunday User mavjud emas")


@router.post('/customer/')
def create_customer(user: CustomerSchema):
    customer_create(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email
    )
    return {"message":"User Yaratildi!", "status":status.HTTP_201_CREATED}


@router.put('/customer/{customer_id}')
def put_customer(customer_id: int, customerschema: CustomerSchema):
    if customer(customer_id):
        customer_update(
            customer_id=customer_id,
            first_name=customerschema.first_name,
            last_name=customerschema.last_name,
            email=customerschema.email,
        )   
        return {"message":"Yangilandi!", "status":status.HTTP_200_OK}
    raise HTTPException(404, "Bunday User mavjud emas")


@router.patch('/customer/{customer_id}')
def patch_customer(customer_id: int, customerschema: CustomerSchemaPatch):
    if customer(customer_id):
        customer_update(
            customer_id=customer_id,
            first_name=customerschema.first_name,
            last_name=customerschema.last_name,
            email=customerschema.email,
        )   
        return {"message":"Yangilandi!", "status":status.HTTP_200_OK}
    raise HTTPException(404, "Bunday User mavjud emas")


@router.delete('/customer/{customer_id}')
def delete_user(customer_id: int):
    if customer(customer_id):
        customer_delete(customer_id)
        return {"message":f"{customer_id} li User Chopildi !!!", "status": status.HTTP_204_NO_CONTENT}
    raise HTTPException(404, "Bunday User mavjud emas")
