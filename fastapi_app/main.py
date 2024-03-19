from fastapi import FastAPI
from models import Item, items

app = FastAPI()

@app.get("/")
async def home():
    """Home function"""
    return {"message": "Hello world!"}

@app.get("/items")
def return_items():
    return {"Items": items}

@app.get("/items/{item_id}")
def get_item(item_id:int):
    if item_id in items:
        return items[item_id]
    else:
        return {"message": "id not found"}

@app.put("/items/{item_id}")
def add_item(item_id:int, item: Item):
    """End point for adding a new todo item"""
    items[item_id] = item
    return {"Todo":item.name, "Id": item_id}
    
