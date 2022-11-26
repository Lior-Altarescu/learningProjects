from app.db import Redis
import uuid


class Controller(object):
    def __init__(self):
        self._r=Redis()

    def saveItem(self,json_item):
        uniqId=str(uuid.uuid1())
        if json_item['price'] > 0:
            self._r.setItem(uniqId,json_item)
            return uniqId
        return "Price must be greater the 0"

    def deleteAllItems(self):
        numOfkeys= len(self._r.getAllKeys())
        if (numOfkeys==0): return "no items in redis"

        self._r.deleteAllItems()
        return f"deleted {numOfkeys} keys"


    def deleteItem(self,item):
        if self.getItem(item):
            return self._r.deleteItem(item)
        return "item not found"
        

    def getItem(self,item):
        return self._r.getItem(item)
