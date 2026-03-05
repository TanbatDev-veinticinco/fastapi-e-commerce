from fastapi import APIRouter, HTTPException
from schemas.product import ProductCreate, ProductOut, ProductUpdate
from services import product_service


router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate):
    return product_service.create_product(product)

@router.get("/", response_model=list[ProductOut])
def get_products():
    return product_service.get_all_products()

@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, data: ProductUpdate):
    try:
        return product_service.update_product(product_id, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{product_id}")
def delete_product(product_id: int):
    try:
        return product_service.delete_product(product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))     
    
