from storage import db


def add_to_cart(user_id: int, product_id: int, quantity: int):

    if quantity <= 0:
        raise ValueError("Quantity must be grater than Zero")

    if product_id not in db.products:
        raise ValueError("Product not found")
    
    product = db.products[product_id]

    if quantity > product["stock"]:
        raise ValueError("Not enough stock")    
    
    if user_id not in db.carts:
        db.carts[user_id] = {"items": []}

    cart = db.carts[user_id]

    for item in cart["items"]:
        if item["product_id"] == product_id:
            
            if item["quantity"] + quantity > product["stock"]:
                raise ValueError("Adding this quantity exceed stock")
            
            item["quantity"] += quantity
            return calculate_cart(user_id)
        
    cart["items"].append({
        "product_id": product_id,
        "quantity": quantity
    })

    return calculate_cart(user_id)

def calculate_cart(user_id: int):
    cart = db.carts[user_id]

    items_with_price = []
    total_price = 0

    for item in cart["items"]:
        product = db.products[item["product_id"]]

        subtotal = product["price"] * item["quantity"]
        total_price += subtotal

        items_with_price.append({
            "product_id": item["product_id"],
            "quantity": item["quantity"],
            "price": product["price"],
            "subtotal": subtotal,
        })

    return {
        "user_id": user_id,
        "items": items_with_price,
        "total_price": total_price
    }



def get_cart(user_id: int):
    if user_id not in db.carts:
        return {
            "user_id": user_id,
            "items": [],
            "total_price": 0
        }
    
    return calculate_cart(user_id)


def remove_from_cart(user_id: int, product_id: int):
    if user_id not in db.carts:
        raise ValueError("Cart does not exist")
    
    cart = db.carts[user_id]

    cart["items"] = [
        item for item in cart["items"]
        if item["product_id"] != product_id
    ]

    return calculate_cart(user_id)


