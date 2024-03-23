from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    checked: Optional[bool] = False 

items = {}


class UpdateCheckedStatus(BaseModel):
    checked: bool
