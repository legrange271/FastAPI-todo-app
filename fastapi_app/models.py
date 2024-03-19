from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    checked: Union[bool, None] = None

items = {}