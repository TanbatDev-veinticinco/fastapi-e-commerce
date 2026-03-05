from storage import db
from datetime import datetime


def create_product(data):

    new_id = db.products_counter

    new_product = {
        "id": new_id,
        "name": data.name,
        "price": data.price,
        "category": data.category,
        "description": data.description,
        "stock": data.stock,
        "vendor_id": data.vendor_id,
        "created_at": datetime.utcnow(),
    }

    db.products[new_id] = new_product
    db.products_counter += 1

    return new_product


def get_all_products():
    return list(db.products.values())


def get_product(product_id: int):
    if product_id not in db.products:
        raise ValueError("Product not found")

    return db.products[product_id]


def update_product(product_id: int, data):
    if product_id not in db.products:
        raise ValueError("Product not found")

    product = db.products[product_id]

    for key, value in data.model_dump(exclude_unset=True).items():
        product[key] = value

    return product


def delete_product(product_id: int):
    if product_id not in db.products:
        raise ValueError("product not found")

    return db.products.pop(product_id)    