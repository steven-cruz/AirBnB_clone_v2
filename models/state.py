#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
import sqlalchemy
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def cities(self):
            """Setter Method to list cities"""
            city_list = []
            for key, value in models.storage.all().items():
                try:
                    if value.state_id == self.id:
                        city_list.append(value)
                except BaseException:
                    pass
            return city_list
    else:
        cities = relationship('City', cascade='all, delete', backref='state')
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
