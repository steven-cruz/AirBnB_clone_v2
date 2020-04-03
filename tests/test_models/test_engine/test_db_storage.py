#!/usr/bin/python3
"""test for databasse storage"""
import unittest
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from os import getenv
import pep8
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
import os
import MySQLdb
import json
import models


@unittest.skipIf(type(models.storage) != DBStorage,
                 "Testing DBStorage")
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

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.db = DBStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.db

    def test_attributes(self):
        """Test if exists attributes"""
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))

    def test_functions(self):
        """Test if exists the functions"""
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))
        self.assertTrue(hasattr(DBStorage, '__init__'))

    def test_pep8_FileStorage(self):
        """pep8 validation"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    def test_for_state(self):
        """Check if create the state"""
        new_state = State(name="TestStates")
        new_state.save()
        if new_state.id in models.storage.all():
            self.assertTrue(new_state.name, "TestStates")

    def test_for_user(self):
        """Check if create the user"""
        new_user = State(email="TestUser")
        new_user.save()
        if new_user.id in models.storage.all():
            self.assertTrue(new_user.email, "TestUser")

    def test_for_amenities(self):
        """Check if create the amenities"""
        new_amenities = State(name="TestAmenity")
        new_amenities.save()
        if new_amenities.id in models.storage.all():
            self.assertTrue(new_amenities.name, "TestAmenity")

if __name__ == "__main__":
    unittest.main()
