#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''

    def test_Amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        '''
            Test that Amenity class had name attribute.
        '''
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())


if __name__ == "__main__":
    unittest.main()