#!/usr/bin/python3
"""test for databasse storage"""
import unittest
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from os import getenv
import MySQLdb
import pep8
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from models import storage
import os
import MySQLdb


class TestDBStorage(unittest.TestCase):
    '''test the db'''

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run if storage is file")
    def setUp(self):
        """set up for test"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_DB"))
            self.cursor = self.db.cursor()
    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run")
    def tearDown(self):
        """do the teardown"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run")
    def test_attributes_DBStorage(self):
        """Test the methods"""
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't")
    def test_pep8_DBStorage(self):
        """pep"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(pep.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
