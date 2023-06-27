from fastapi import APIRouter
from ... import database, schema, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from . import user_service
from uuid import UUID
from ..authentication.oauth2 import *

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schema.ShowUser)
def create_user(request: schema.User,db: Session = Depends(get_db)):
    return user_service.create(request,db)

@router.get('/{id}',response_model=schema.ShowUser)
def get_user(id:UUID,db: Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    return user_service.show(id,db)