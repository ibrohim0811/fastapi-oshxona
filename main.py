from fastapi import FastAPI


from database import (
    create_table, create_item, 
    create_orders, create_user,
    create_order_item
)
from api.category import router as category
from api.item import router as item
from api.order import router as order
from api.user import router as user

create_table()
create_user()
create_item()
create_orders()
create_order_item()

app = FastAPI()
app.include_router(category)
app.include_router(item)
app.include_router(order)
app.include_router(user)

@app.get('/root/')
async def root():
    return {"message":"ok"}