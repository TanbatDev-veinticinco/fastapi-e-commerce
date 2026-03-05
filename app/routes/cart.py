from fastapi import APIRouter, HTTPException
from services import cart_service
from schemas.cart import CartCreate, CartOut


router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/add/{user_id}", response_model=CartOut)
def add_to_cart(user_id: int, data: CartCreate):
    try:
        return cart_service.add_to_cart(
            user_id,
            data.product_id,
            data.quantity
        )
    
    except ValueError as e:
        raise HTTPException(status_code= 400, detail=str(e))
    
@router.get("/{user_id}", response_model=CartOut)
def get_cart(user_id: int):

    return cart_service.get_cart(user_id)   

@router.delete("/remove/{user_id}/{product_id}", response_model=CartOut)
def remove_cart(user_id: int, product_id: int):

    try:
        return cart_service.remove_from_cart(user_id, product_id)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))