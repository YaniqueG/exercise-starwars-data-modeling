import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,ForeignKey('User.id'))
    user_to_id = Column(Integer,ForeignKey('User.id'))
    

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    url = Column(String(250))
    post_id = Column(String(250),ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(String(250),primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
