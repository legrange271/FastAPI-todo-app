from fastapi import FastAPI, Response, status
from models import Item, items

app = FastAPI()

@app.get("/", status_code=200)
def home():
    """Specify basic app functionality"""
    return {"message": "Hello world!"}

@app.get("/items", status_code=200)
def get_items():
    """Endpoint for listing all items"""
    return {"Items": items}

@app.get("/items/{item_id}", status_code=200)
def get_item(item_id:int, response:Response):
    """Endpoint for getting an item by id"""
    if item_id in items:
        return items[item_id]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "id not found"}

@app.post("/items/{item_id}", status_code=201)
def add_item(item_id:int, item: Item, response:Response):
    """End point for adding a new todo item"""
    if item_id in items:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Item already exists"}
    else:
        items[item_id] = item
        return {"Todo":item.name, "Id": item_id}
    
