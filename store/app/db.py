import redis
import logging
import json

logger = logging.getLogger('redis')

class Redis:
    def __init__(self):
        self._port=6379
        self._hostname="localhost"
        self._pool=redis.ConnectionPool(host=self._hostname, port=self._port, db=0,max_connections=10)
        try:
            self._cursor = redis.Redis(connection_pool=self._pool,decode_responses=True)
            if self._cursor.ping():
                logger.info("successfully connected to redis")
            else:
                logger.warning("problem connecting to redis")
        except Exception as e:
            logger.error(e)
                

    def setItem(self,key,value):
        if not self._cursor.set(key,json.dumps(value)):
            logger.error("problem inserting data")

    def getItem(self,key):
        if not self._cursor.get(key):
            return "No Key found"
        return json.loads(self._cursor.get(key))

    def deleteAllItems(self):
        for key in self._cursor.keys():
            self._cursor.delete(key)
    
    def deleteItem(self,key):
        if self.getItem(key):
            self._cursor.delete(key)
            return "done"
        return "Key not found"

    def getAllKeys(self):
        return self._cursor.keys()