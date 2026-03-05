from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float
    created_at: datetime


class OrderItemOut(BaseModel):
    product_id: int
    quantity: int
    price: float
    subtotal: float


class OrderOut(BaseModel):
    id: int
    user_id: int
    quantity: int
    items: list[OrderItemOut]
    total_price: float
    status: str
    created_at: datetime    