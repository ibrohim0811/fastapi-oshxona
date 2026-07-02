from fastapi import APIRouter, status, HTTPException
from typing import List

from schemas.category import CategorySchema, CategoryCreateSchema, CategoryPatchSchema, CategoryPutSchema
from crud.categorydb import (
categories, category_detail, 
category_create, category_delete, 
category_update
)

router = APIRouter(
    tags=["category"]
)


@router.get("/categories", response_model=List[CategorySchema])
def get_categories():
    db_data = categories()
    formatted_data = [{"id": row[0], "name": row[1]} for row in db_data]
    return formatted_data


@router.get("/category/{category_id}", response_model=List[CategorySchema])
def get_category_id(category_id: int):
    data = category_detail(category_id)
    if data:
        formatted_data = [{"id": data[0], "name": data[1]}]
        return formatted_data
    raise HTTPException(404, "Bunday kategoriya mavjud emas!")


@router.post("/category")
def create_category(category: CategoryCreateSchema):
    try:
        category_create(category_name=category.name)
        return {"message": "Kategoriya qo'shildi!", "status":status.HTTP_201_CREATED}
    except Exception as e:
        print(e)
        return {"message":"Serverda xatolik!", "status":status.HTTP_500_INTERNAL_SERVER_ERROR}
    

@router.put('/category/{category_id}')
def update_category_put(category_id: int, category: CategoryPutSchema):
    if category_detail(category_id):
        category_update(category_id, category.name)
        return {"message":"Yangilandi", "status": status.HTTP_200_OK}
    raise HTTPException(404, "Kiritilgan Kategoriya topilmadi!")


@router.patch('/category/{category_id}')
def update_category_patcht(category_id: int, category: CategoryPatchSchema):
    if category_detail(category_id):
        category_update(category_id, category.name)
        return {"message":"Yangilandi", "status": status.HTTP_200_OK}
    raise HTTPException(404, "Kiritilgan Kategoriya topilmadi!")


@router.delete('/category/{category_id}')
def delete_category(category_id: int):
    if category_detail(category_id):
        category_delete(category_id)
        return {"message":f"{category_id} id raqamli Kategoriya O'chirildi !", "status": status.HTTP_204_NO_CONTENT}
    raise HTTPException(404, "Kiritilgan Kategoriya topilmadi!")