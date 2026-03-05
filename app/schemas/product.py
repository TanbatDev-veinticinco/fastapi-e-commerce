from pydantic import BaseModel
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    price: float
    category: str
    description: str
    stock: int
    vendor_id: int

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    category: str | None = None
    description: str | None = None
    stock: str | None = None


class ProductOut(BaseModel):    
    id: int
    name: str
    price: float
    description: str
    category: str
    stock: int
    vendor_id: int
    created_at: datetime
       
