import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))

    user = relationship("User", back_populates = "favorites")

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)

    favorites = relationship("Favorites", back_populates = "user")
    post = relationship("Post", back_populates = "user")
    comment = relationship("Comment", back_populates = "user")
    characters = relationship("Characters", back_populates = "user")
    planets = relationship("Planets", back_populates = "user")


    def to_dict(self):
        return {}

    def login(self):
        return {}
    
    def save_planets(self):
        return {}

    def save_characters(self):
        return {}

class Characters(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(String) 
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    skin_color = Column(String)
    created = Column(String)
    edited = Column(String)
    species = Column(String)
    starships = Column(String)
    url = Column(String)
    vehicles = Column(String)

    user = relationship("User", back_populates = "characters")

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String)
    created = Column(String)
    diameter = Column(String)
    edited = Column(String)
    films = Column(String)
    gravity = Column(String)
    name = Column(String)
    orbital_period = Column(String)
    population = Column(String)
    residents = Column(String)
    rotation_period = Column(String)
    surface_water = Column(String)
    terrain = Column(String)
    url = Column(String)

    user = relationship("User", back_populates = "planets")

    def to_dict(self):
        return {}


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type_media = Column(Enum)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))

    post = relationship("Post", back_populates = "media")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates = "post")
    media = relationship("Media", back_populates = "post")
    comment = relationship("Comment", back_populates = "post")


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    user = relationship("User", back_populates = "comment")
    post = relationship("Post", back_populates = "comment")


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
