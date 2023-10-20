#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity inherits from BaseModel and Base"""
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
