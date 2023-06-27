from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from ... import schema, database, models
from sqlalchemy.orm import Session
from . import blog_service
from uuid import UUID
from ..authentication.oauth2 import *

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/', response_model=List[schema.ShowBlog])
def all(db: Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    return blog_service.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schema.Blog, db: Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    return blog_service.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:UUID, db: Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    return blog_service.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:UUID, request: schema.Blog, db: Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    return blog_service.update(id,request, db)


@router.get('/{id}', status_code=200, response_model=schema.ShowBlog)
def show(id:UUID, db: Session = Depends(get_db),current_user:schema.User=Depends(get_current_user)):
    return blog_service.show(id,db)

