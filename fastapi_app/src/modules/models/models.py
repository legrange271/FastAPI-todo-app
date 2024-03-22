from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    checked: Optional[bool] = None

# Here we define a simple in memory non persistent file store 
# TODO: add a start up and end command to save this and keep it secure
items = {}