import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum


Base = declarative_base()

class Type_Media(enum.Enum):
    image = "image"
    video = "video"



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False,unique=True)
    firstname=Column(String(30))
    lastname=Column(String(30))
    email=Column(String(40),nullable=False,unique=True)
    comments= relationship ('Comment',back_populates='author_relationship')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200),nullable=False)
    author = Column(Integer,ForeignKey('user.id'))
    author_relationship = relationship ('User',back_populates='comments')
    post_id= Column(Integer,ForeignKey('post.id'))

class Post(Base):
    __tablename__='post'
    id= Column(Integer,primary_key=True)
    user_id= Column(Integer,ForeignKey('user.id'))

class Media(Base):
    __tablename__='media'
    id= Column(Integer,primary_key=True)
    type_data = Column(Enum(Type_Media))
    url= Column(String(100))
    post_id=Column(Integer,ForeignKey('post.id'),unique=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
