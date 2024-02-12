from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from app.database import get_db
from .. import models, oauth2, schemas, utils
from ..database import get_db



router = APIRouter(tags=["Authentification"])

@router.post("/login", response_model=schemas.Token)
def login(user_credential:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()
    
    if not user:
        raise HTTPException(status_code=403, detail="User not found")
    
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid credentials")
    
    #if user is None or not utils.verify(user_credential.password, user.password):
    #    raise HTTPException(status_code=400, detail="Invalid credentials")
    #return {"access_token": utils.create_access_token(data={"sub": user.email}), "token_type": "bearer"}
    
    access_token = oauth2.create_access_token(data={ "User_id": user.id})
    return {"access_token": access_token, 
            "token_type": "bearer"}
