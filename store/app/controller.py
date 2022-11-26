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
        # for key in self.returnAllIKeys():
        #     if str(json_item['name']).lower() == str(self.getItem(key)['name']).lower():
        #         return "product already exists"
        if self.returnKeyByName(json_item['name']):
            return "product already exists"


        uniqId=uuid.uuid1().int
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

    def returnAllIKeys(self):
        """
        Return all Items
        """
        return self._r.getAllKeys()

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
        print(item)
        return self._r.getItem(item)

    def changeItemAmount(self,bItem,whatTodo):
        try:
            value=self.getItem(self.returnKeyByName(bItem['name']))
            print(value)
            if value and bItem['amount'] > 0:
                if whatTodo == "reduce":
                    value['stock']-=bItem['amount']
                    value['amountSold']+=bItem['amount']
                else:
                    value['stock']+=bItem['amount']
                    value['amountSold']-=bItem['amount']
                self._r.setItem(self.returnKeyByName(bItem['name']),value)
                return value
            return "Couldn't find item"
        except Exception as e:
            return False

    # def reduceItemAmout(self,bItem):
    #     try:
    #         value=self.getItem(self.returnKeyByName(bItem['name']))
    #         if value and bItem['amount'] > 0:
    #             value['stock']-=bItem['amount']
    #             value['amountSold']+=bItem['amount']
    #             self._r.setItem(self.returnKeyByName(bItem['name']),value)
    #             return value
    #         return "Couldn't find item"
    #     except Exception as e:
    #         return False

    # def increaseItemAmount(self,bItem):
    #     try:
    #         value=self.getItem(self.returnKeyByName(bItem['name']))
    #         if value and bItem['amount'] > 0:
    #             value['stock']+=bItem['amount']
    #             value['amountSold']-=bItem['amount']
    #             self._r.setItem(self.returnKeyByName(bItem['name']),value)
    #             return value
    #         return "Couldn't find item"
    #     except Exception as e:
    #         print(e)
    #         return False

    def returnKeyByName(self,name):
        for key in self.returnAllIKeys():
            if str(name).lower() == str(self.getItem(key)['name']).lower():
                return key