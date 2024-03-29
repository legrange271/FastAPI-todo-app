from fastapi import APIRouter, Response, status
from modules.models.models import Item, items, UpdateCheckedStatus
from modules.utils.id_gen import gen_unique_id

router = APIRouter()

@router.get("/items", status_code=200)
def get_items():
    """Endpoint for listing all items"""
    return {"Items": items}

@router.post("/items", status_code=201)
def add_item(item: Item):
    """End point for adding a new todo item

    INPUTS 
        item_id : id of item you wish to create
        item : object with pydantic model you wihs to create
        resposne : response object to be returned
    
    Ouputs
        response object containing either the item or a id not found 
    """
    # Generate a unique id
    item_id = gen_unique_id()
    items[item_id] = item
    return {"id": item_id, "name":item.name, "checked":item.checked}

@router.get("/items/{item_id}", status_code=200)
def get_item(item_id:str, response:Response):
    """Endpoint for getting an item by id
    
    INPUTS 
        item_id : id of item you wish to get  
        resposne : response object to be returned

    Ouputs
        response object containing either the item or a id not found 
    """
    if item_id in items:
        return items[item_id]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "ID not found"}

    
@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id:str, response:Response):
    """End point for deleting a new todo item

    INPUTS 
        item_id : id of item you wish to delete 
        resposne : response object to be returned
    
    Ouputs
        response object containing either the item or a id not found 
    """
    if item_id  not in items:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "ID not found"}
    
    items.pop(item_id) 


@router.put("/items/{item_id}", status_code=201)
def check_item(item_id:str, msg: UpdateCheckedStatus, response:Response):
    """End point for adding a new todo item

    INPUTS 
        item_id : id of item you wish to create
        item : object with pydantic model you wihs to create
        resposne : response object to be returned
    
    Ouputs
        response object containing either the item or a id not found 
    """
    if item_id  not in items:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "ID not found"}
    
    items[item_id].checked = msg.checked
    return {"id": item_id, "name":items[item_id].name, "checked":items[item_id].checked}


### TODO: Add section for checking items to see if they are checked or not