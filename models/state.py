#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")


    @property
    def cities(self):
        """get list of city"""
        city_ls = []
        for i in models.storage.all(City).values():
            if i.state_id == self.id:
                city_ls.append(City)
        return city_ls
