from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float
    created_at: datetime


class OrderOut(BaseModel):
    product_id: int
    quantity: int
    price: float
    quantity: int


class OrderCreate(BaseModel):
    user_id: int

class OrderOut(BaseModel):
    id: int
    user_id: int
    items: list[OrderOut]
    total_price: float
    status: str
    created_at: datetime    