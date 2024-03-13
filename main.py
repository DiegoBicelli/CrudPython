from fastapi import FastAPI
from models import Item
from controllers import create_item, get_all_items, update_item, delete_item, get_item_by_id
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [ 
    "http://localhost:8000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post("/items/")
def add_item(item: Item):
    return create_item(item)

@app.get("/items/")
def read_items():
    return get_all_items()

@app.put("/items/{item_id}")
def update_item_details(item_id: str, item: Item):
    return update_item(item_id, item)

@app.delete("/items/{item_id}")
def remove_item(item_id: str):
    return delete_item(item_id)

@app.get("/items/{item_id}")
def read_item_by_id(item_id: str):
    return get_item_by_id(item_id)
