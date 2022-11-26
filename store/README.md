# Simple Store


This is a simple representaiton of a store . The following steps will show how to install and run the application.   
**This project is for learning purposes only** 

*This works only for python 3
*** 

### Install 
```bash
pip install -r requirments
```

### start the redis docker
```docker 
docker run -d -p 6379:6379 --name redis-store redis
```

### Run the application 
```python 
python store/main.py 
```

# REST API
### Add Item  
```POST /addItem/```
```bash
curl -X POST \
  'http://127.0.0.1:8000/addItem' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "name": "Cola",
  "description":"Great taste",
  "price": 12
}'
```
### Get Item  
```Get /getItem/{itemId}```
```bash
curl -X GET \
  'http://127.0.0.1:8000/getItem/97815f44-6d7d-11ed-afa1-00155d2a54f7' 
```
### Delete Item  
```Put /deleteItem/{itemId}```
```bash
curl -X PUT \
  'http://127.0.0.1:8000/deleteItem/97815f44-6d7d-11ed-afa1-00155d2a54f7' 
```
### Delete All Item  
```Put /deleteAllItems/```
```bash
curl -X PUT \
  'http://127.0.0.1:8000/deleteAllItems'
```

***
Made with :heart: By Lior Altarescu. 