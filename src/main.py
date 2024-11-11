from fastapi import FastAPI
from .database import engine
from .models import Base

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Плохая практика: нет обработки ошибок
    return {"item_id": item_id}