#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'),
                                primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'),
                                primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1027))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night =Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        def __init__(self,*args, **kwargs):
            """ initializes a Place instance """
            super().__init__(*args, **kwargs)

        @property
        def reviews(self):
            """ return Review instance without place_id=current Place.id """
            all_instance = models.storage.all()
            query = []
            for key, val in all_instance.items():
                if key.startswith('Review') and
                    getattr(val, 'place_id') == self.id:
                        query.append(val)
            return query

        @property
        def amenities(self):
            """ return Amenity instance without place_id=current Place.id """
            all_instance = models.storage.all()
            query = []
            for key, val in all_instance.items():
                if key.startswith('Amenity') and
                    getattr(val, 'place_id') == self.id:
                        query.append(val)
            return query

        @amenities.setter
        def amenities(self, amenity=None):
            """ Update amenities in Place """
            all_instances = models.storage.all()
            dicts = {}
            for key, val in all_instances.items():
                if key.startswith('Amenity'):
                    dicts.update({key: val})
            querys = []
            if amenity:
                for amenity in dicts.values():
                    if amenity.place_id == self.id:
                        amenity_ids.append(amenity)
