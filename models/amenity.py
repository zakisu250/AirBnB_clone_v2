#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, Float, Strgin, ForeignKey, Table
from sqlalchemy.orm import relationship
import os
import models.place import place_amenity

class Amenity(BaseModel):
    """ Defines Amenity """
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place-amenities = realtionship('Place', secondary=place_amenity, back_populates='amenities')
    else:
        name = ""
