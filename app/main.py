from fastapi import FastAPI
from routes import product, user, cart, order


app = FastAPI()


app.include_router(product.router)
app.include_router(user.router)
app.include_router(cart.router)
app.include_router(order.router)

@app.get("/")
def root():
    return {"message": "Hello, World!"}