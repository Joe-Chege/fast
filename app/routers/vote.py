from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from app.database import get_db
from .. import models, oauth2, schemas, utils
from ..database import get_db


router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)

@router.post("/{id}", status_code = status.HTTP_201_CREATED)
def create_vote(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    vote = db.query(models.Vote).filter(models.Vote.post_id == id, models.Vote.user_id == current_user.id).first()
    if vote:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "You already voted for this post")
    new_vote = models.Vote(post_id = id, user_id = current_user.id)
    db.add(new_vote)
    db.commit()
    return new_vote