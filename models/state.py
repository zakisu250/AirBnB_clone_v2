#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class initialization """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """ Initialize the states class """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """get list of city"""
        city_ls = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_ls.append(city)
        return city_ls
