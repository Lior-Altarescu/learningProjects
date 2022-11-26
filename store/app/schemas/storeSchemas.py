from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    """
    Schema for Item 
    """
    name: str
    description: Union[str, None] = None
    price: int
    stock: int
    salePercent: float
    amountSold = 0

class buyItem(BaseModel):
    """
    Schema for buying a Item
    """
    name: str
    amount: int