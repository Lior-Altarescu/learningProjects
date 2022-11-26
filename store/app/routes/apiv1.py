from app.schemas.storeSchemas import Item,buyItem
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI,Depends
import logging
from app.controller import Controller
from typing import Union

app = FastAPI()


logger = logging.getLogger('store')


# insert item
@app.post("/addItem/")
def add_item(item: Item, con:Controller = Depends(Controller)):
    """ 
    Forwards the item to controller to save in redis 
    Args:
        item (item) : A item odj
    Retruns status if was able to store     
    """
    return con.saveItem(jsonable_encoder(item))


#delete allitems
@app.put("/deleteAllItems")
async def delete_all_item(con:Controller = Depends(Controller)):
    """ 
    Forwards to controller to delete all items 
    Retruns status if was able to delete 
    """
    logger.info("deleting all keys")
    return con.deleteAllItems()


#get Item
@app.get("/getItem/{itemName}")
async def get_item(itemName: str,con:Controller = Depends(Controller)):
    """ 
    Forwards to controller to get Item by itemId
    Args:
        itemid (str): uuid 
    Retruns the item if was able to find or error message
    """
    logger.info(f"retrieve key {itemName}")
    return con.getItem(itemName)

    

#delete item
@app.put("/deleteItem/{itemName}")
async def delete_item(itemName: str,con:Controller = Depends(Controller)):
    """ 
    Forwards to controller to delete  items 
    Args:
        itemid (str): uuid 
    Retruns status if was able to delete 
    """
    logger.info(f"delete item {itemName}")
    return con.deleteItem(itemName)

@app.post("/buyItem/")
async def but_item(bItem: buyItem,con:Controller = Depends(Controller)):
    """
    Forwords to controller to add amount to item
    """
    return con.changeItemAmount(jsonable_encoder(bItem),"reduce")

@app.post("/returnItem/")
async def return_item(rItem: buyItem,con:Controller = Depends(Controller)):
    """
    Forwords to controller to reduce amount to item
    """
    return con.changeItemAmount(jsonable_encoder(rItem),"increase")