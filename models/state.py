#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.storage == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete", backref="state")
    else:
        name = ''

    if models.storage != 'db':
        @property
        def cities(self):
            """Return list of city"""
            city_ls = []
            for i in models.storage.all(City).values():
                if i.state_id == self.id:
                    city_ls.append(city)
            return city_ls
