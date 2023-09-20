#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.user import User
from models.places import Places
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nulable= False, ForeignKey('places.id')
    user_id = Column(String(60), nullable=False, ForeignKey('places.id'))
