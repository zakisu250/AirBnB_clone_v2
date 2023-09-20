#!/usr/bin/python3
"""
New engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State 
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """DB Storage Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of Engine"""
        user = getenv(HBNB_MYSQL_USER)
        pwd = getenv(HBNB_MYSQL_PWD)
        host = getenv(HBNB_MYSQL_HOST)
        db = getenv(HBNB_MYSQL_DB)
        env = getenv(HBNB_ENV)
        self.__engin = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        res = {}
        if cls is None:
            obj = [User, State, City, Amenity, Place, Review]
        else:
            obj = self.__session.query(cls).all()
        for i in obj:
            k = f"{i.__class__.__name__}.{i.id}"
            res[k] = i
        return res

    def new(self, obj):
        """Add the object to DB"""
        self.__session.add(ob)

    def save(self):
        """commit all cham=nge of the DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)


    def reload(self):
        """
        drop and recreate all tables in the database"""
        Base.metadata.create_all(bing=self.__engine)
        self.__session = scoped_session(sessionmaker(expire_on_commit=False)(bind=self.__engine))
