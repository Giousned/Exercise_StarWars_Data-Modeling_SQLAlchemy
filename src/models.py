import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)

    favorites = relationship("Favorites", back_populates = "user")
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

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))

    user = relationship("User", back_populates = "favorites")

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(String, nullable=True) 
    eye_color = Column(String, nullable=True)
    films = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    hair_color = Column(String, nullable=True)
    height = Column(String, nullable=True)
    homeworld = Column(String, nullable=True)
    mass = Column(String, nullable=True)
    skin_color = Column(String, nullable=True)
    created = Column(String, nullable=True)
    edited = Column(String, nullable=True)
    species = Column(String, nullable=True)
    starships = Column(String, nullable=True)
    url = Column(String, nullable=True)
    vehicles = Column(String, nullable=True)

    user = relationship("User", back_populates = "characters")

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String, nullable=True)
    created = Column(String, nullable=True)
    diameter = Column(String, nullable=True)
    edited = Column(String, nullable=True)
    films = Column(String, nullable=True)
    gravity = Column(String, nullable=True)
    name = Column(String, nullable=False)
    orbital_period = Column(String, nullable=True)
    population = Column(String, nullable=True)
    residents = Column(String, nullable=True)
    rotation_period = Column(String, nullable=True)
    surface_water = Column(String, nullable=True)
    terrain = Column(String, nullable=True)
    url = Column(String, nullable=True)

    user = relationship("User", back_populates = "planets")

    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
