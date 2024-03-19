from fastapi import FastAPI, Response, status
from models import Item, items

app = FastAPI()

@app.get("/", status_code=200)
def home():
    """Home function for basic functoinality"""
    return {"message": "Hello world!"}

@app.get("/items", status_code=200)
def return_items():
    return {"Items": items}

@app.get("/items/{item_id}", status_code=200)
def get_item(item_id:int, response:Response):
    if item_id in items:
        return items[item_id]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "id not found"}

@app.post("/items/{item_id}", status_code=201)
def add_item(item_id:int, item: Item, response:Response):
    """End point for adding a new todo item"""
    items[item_id] = item
    return {"Todo":item.name, "Id": item_id}
    
