from fastapi import FastAPI

from model import Product

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "FastAPI is running!"
    }
    
products = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=1200.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=800.99, quantity=20)
]
    
@app.get("/products")
def get_all_products():
    return products

