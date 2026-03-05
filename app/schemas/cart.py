from pydantic import BaseModel


class CartCreate(BaseModel):
    product_id: int
    quantity: int

class CartItemOut(BaseModel):
    product_id: int
    quantity: int
    price: float
    subtotal: float    

class CartOut(BaseModel):
    user_id: int
    items: list[CartItemOut]
    total_price: float
