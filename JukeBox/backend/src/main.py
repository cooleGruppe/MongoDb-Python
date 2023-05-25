from pymongo import MongoClient
from fastapi import FastAPI
from dotenv import dotenv_values
from src.routes import router as book_router



config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    # app.mongodb_client = MongoClient(config["DB_CONNECTION"])
    # app.database = app.mongodb_client[config["DB_NAME"]]
    app.mongodb_client = MongoClient("mongoDb")
    app.database = app.mongodb_client["JukeBox"]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}

app.include_router(book_router, tags=["songs"], prefix="/songs")

