from sqlalchemy.orm import Session
from ... import models, schema
from fastapi import HTTPException,status
from uuid import UUID

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schema.Blog,db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:UUID,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:UUID,request:schema.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return 'updated'

def show(id:UUID,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog