#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if of.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ""
        name = ""
