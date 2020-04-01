#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """class to manage MySql DB storage"""
    __engine = None
    __session = None

    def __init__(self):
        """engine init"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ show all results """
        result = []
        if cls:
            result = self.__session.query(cls).all()
        else:
            cl_list = [User, Place, State, City, Amenity, Review]
            for class_name in cl_list:
                temp = self.__session.query(class_name).all()
                result.extend(temp)

        result_dict = {}
        for res in result:
            key = "{}.{}".format(type(res).__name__, res.id)
            value = res
            result_dict[key] = value
        return result_dict

    def new(self, obj):
        """ add new object to session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ save changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                bind=self.__engine, expire_on_commit=False
            )
        )
        self.__session = Session()
