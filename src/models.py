from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    body = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blog', back_populates="creator")