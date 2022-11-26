import redis
import logging
import json

logger = logging.getLogger('redis')

class Redis:
    """
    Class to interact with Redis .The class opens a connection to a local docker redis with max connections of 10 connections
    """

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
        """Store value by key . Json values are stored as strings"""
        if not self._cursor.set(key,json.dumps(value)):
            logger.error("problem inserting data")

    def getItem(self,key):
        """Returns key if found"""
        if not self._cursor.get(key):
            return "No Key found"
        return json.loads(self._cursor.get(key))

    def deleteAllItems(self):
        """Iterates over all keys and deletes them """
        for key in self._cursor.keys():
            self._cursor.delete(key)
    
    def deleteItem(self,key):
        """Deletes Item if exists"""
        if self.getItem(key):
            self._cursor.delete(key)
            return "done"
        return "Key not found"

    def getAllKeys(self):
        """Returns all keys in redis"""
        return self._cursor.keys()