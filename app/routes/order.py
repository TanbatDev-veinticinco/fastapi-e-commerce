from fastapi import APIRouter, HTTPException
from schemas.order import OrderCreate, OrderItemOut, OrderOut
from services import order_service


router = APIRouter(prefix="/Orders", tags=["Orders"])

@router.post("/{user_id}", response_model=OrderOut)
def create_order(user_id: int):
    try: 
        return order_service.create_order(user_id)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))