from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    """
    Schema for Item 
    """
    name: str
    description: Union[str, None] = None
    price: int