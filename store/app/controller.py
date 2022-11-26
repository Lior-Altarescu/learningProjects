from app.db import Redis
import uuid


class Controller(object):
    """
    The job of the controller is to communite with the db module and process requests from the routes modules
    """
    def __init__(self):
        """Initate Redis connection pool"""
        self._r=Redis()

    def saveItem(self,json_item):
        """ 
        Stores json value item in redis
        Args:
            json_item (json): item by itemSchema class
        Retruns the uuid that was created if the item was saved 
        """
        uniqId=str(uuid.uuid1())
        if json_item['price'] > 0:
            self._r.setItem(uniqId,json_item)
            return uniqId
        return "Price must be greater the 0"

    def deleteAllItems(self):
        """ 
        Checks if there are any keys in redis and if deletes them all 
        Retruns deleted status 
        """
        numOfkeys= len(self._r.getAllKeys())
        if (numOfkeys==0): return "no items in redis"

        self._r.deleteAllItems()
        return f"deleted {numOfkeys} keys"


    def deleteItem(self,itemId):
        """ 
        Deletes a item by id if exists
        Args:
            itemId (str): uuid
        Retruns the status of the deleted item 
        """
        return self._r.deleteItem(itemId)
     
        

    def getItem(self,item):
        """ 
        Returns item by id if exists
        Args:
            itemId (str): uuid
        Retruns the json item 
        """
        return self._r.getItem(item)
