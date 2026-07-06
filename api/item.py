from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from models.item import items, item, item_create, item_update, item_delete
from schemas.items import ItemSchema, ItemPatchSchema
from database import get_db

router = APIRouter(
    tags=['items']
)

@router.get('/items', response_model=List[ItemSchema])
def get_items(db: Session = Depends(get_db)):
    data = items(db=db)
    formatted_data = [{"id": row[0], "name": row[1], "about": row[2], "price": row[3], "is_active": row[4], "category_id": row[5]} for row in data]
    return formatted_data


@router.get('/item/{item_id}', response_model=List[ItemSchema])
def get_item(item_id: int, db: Session = Depends(get_db)):
    data = item(item_id=item_id, db=db)
    if data:
        formatted_data = [{"id": data[0], "name": data[1], "about": data[2], "price": data[3], "is_active": data[4], "category_id": data[5]}]
        return formatted_data
    raise HTTPException(404, "Bunday item mavjud emmas!")

@router.post('/item/')
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    item_create(name=item.name, about=item.about, price=item.price, category_id=item.category_id, db=db)   
    return {"message": "Yaratildi !", "status":status.HTTP_201_CREATED}


@router.put('/item/{item_id}')
def put_item(item_id: int, item: ItemSchema, db: Session = Depends(get_db)):
    item_update(
        item_id=item_id,
        name=item.name,
        about=item.about,
        is_active=item.is_active,
        price=item.price,
        category_id=item.category_id,
        db=db
    )
    return {"message":"Yangilandi!", "status":status.HTTP_200_OK}


@router.patch('/item/{item_id}')
def patch_item(item_id: int, item: ItemPatchSchema, db: Session = Depends(get_db)):
    item_update(
        item_id=item_id,
        name=item.name,
        about=item.about,
        is_active=item.is_active,
        price=item.price,
        category_id=item.category_id,
        db=db
    )
    return {"message":"Yangilandi!", "status":status.HTTP_200_OK}


@router.delete('/item/{item_id}')
def patch_item(item_id: int, db: Session = Depends(get_db)):
    if item(item_id):
        item_delete(item_id, db=db)
        return {"message":"O'chirildi!", "status":status.HTTP_204_NO_CONTENT}
    raise HTTPException(404, "Kiritilgan mahsulot topilmadi!")