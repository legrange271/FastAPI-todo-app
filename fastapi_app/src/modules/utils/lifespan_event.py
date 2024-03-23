import os
import json 
from contextlib import asynccontextmanager

from fastapi import FastAPI
from modules.models.models import items, Item

@asynccontextmanager
async def lifespan(app: FastAPI):
    global items
    data_path = os.path.join(os.getcwd(), "data", "database.json")
    if os.path.exists(data_path):
        with open(data_path, "r") as file:
            items_dict = json.load(file)

        for item_id, item in items_dict.items():
            items[item_id]= Item(name=item["name"], checked=item["checked"])


    yield

    items_dict = {item_id: item.dict() for item_id, item in items.items()}

    with open(data_path, "w") as file:
        json.dump(items_dict, file)