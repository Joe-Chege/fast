from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.database import engine, get_db
from . import models
from . import schemas
from . import utils
from . import oauth2
from app.config import settings
from  app.routers import post, user, auth







#models.Base.metadata.create_all(bind=engine)

while True:
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="joechege",
                                      host="localhost",
                                      port="5432",
                                      database="PythonApi",
                                      cursor_factory=RealDictCursor)
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print("Database connection successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(3)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

my_posts = [
    {"title": "Building Scalable Systems", "content": "Architecting for growth and performance", "published": True,
     "id": 12},
    {"title": "Quantum Computing Insights", "content": "The future of computing", "published": True, "id": 13},
    {"title": "Blockchain Revolution", "content": "Decentralizing the future", "published": False, "id": 14},
    {"title": "Augmented Reality Experiences", "content": "Enhancing reality with AR", "published": True, "id": 15},
]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"Message": "Word of the world/n Yo will make it in this life"}


