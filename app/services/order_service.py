from app.storage import db
from datetime import datetime


def create_order(user_id: int):

    if user_id not in db.users:
        raise ValueError("user not found")
    
    if user_id not in db.carts:
        raise ValueError("Cart does not exist")
    
    cart = db.carts[user_id]

    if not cart["items"]:
        raise ValueError("cart is empty")
    
    order_items = []
    total_price = 0

    for item in cart["items"]:
        product = db.products[item["product_id"]]

        if item["quantity"] > product ["stock"]:
            raise ValueError("Not enough stock")

        subtotal = product["price"] * item["quantity"]
        total_price += subtotal

        product["stock"] -= item["quantity"]

        order_items.append({
            "product_id": item["product_id"],
            "quantity": item["quantity"],
            "price": product["price"],
            "subtotal": subtotal
        })

    new_order_id = db.orders_counter

    new_order = {
        "id": new_order_id,
        "user_id": user_id,
        "items": order_items,
        "total_price": total_price,
        "status": "completed",
        "created_at": datetime.utcnow()
    }

    db.orders[new_order_id] = new_order
    db.orders_counter += 1

    return new_order
