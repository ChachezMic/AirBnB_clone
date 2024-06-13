#!/usr/bin/python3
"""Test Amenity"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Testing Amenity"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Naming"""
        new = self.value()
        self.assertEqual(type(new.name), str)
