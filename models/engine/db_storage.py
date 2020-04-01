#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """class to manage MySql DB storage"""
    __engine = None
    __session = None

    def __init__(self):
        """engine init"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ show all results """
        result = []
        if cls is not None:
            result = self.__session.query(cls).all()
        else:
            cl_list = [User, Place, State, City, Amenity, Review]
            for class_name in cl_list:
                temp = self.__session.query(class_name)
                for res in temp:
                    result.append(res)

        result_dict = {}
        for res in result:
            key = "{}.{}".format(type(res).__name__, res.id)
            result_dict[key] = res
        return result_dict

    def new(self, obj):
        """ add new object to session """
        self.__session.add(obj)

    def save(self):
        """ save changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session
