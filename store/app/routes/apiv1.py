from app.schemas.itemsSchema import Item
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI,Depends
import logging
from app.controller import Controller

app = FastAPI()


logger = logging.getLogger('store')


# insert item
@app.post("/addItem/")
def add_item(item: Item, con:Controller = Depends(Controller)):
    return con.saveItem(jsonable_encoder(item))


#delete allitems
@app.put("/deleteAllItems")
async def delete_all_item(con:Controller = Depends(Controller)):
    logger.info("deleting all keys")
    return con.deleteAllItems()


#get Item
@app.get("/getItem/{itemId}")
async def get_item(itemId: str,con:Controller = Depends(Controller)):
    logger.info(f"retrieve key {itemId}")
    return con.getItem(itemId)

    

#delete item
@app.put("/deleteItem/{itemId}")
async def delete_item(itemId: str,con:Controller = Depends(Controller)):
    logger.info(f"delete item {itemId}")
    return con.deleteItem(itemId)
