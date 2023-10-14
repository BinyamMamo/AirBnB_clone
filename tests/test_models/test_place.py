#!/usr/bin/python3

import inspect
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from models.place import Place
from models import place
from unittest import mock


class TestPlaceDocs(unittest.TestCase):
    """ Tests the Place class for documentation and style"""

    # __funcs = inspect.getmembers(Place, predicate=inspect.isfunction)

    # def test_func_docs(self):
    #     """ Tests if all methods of Place are documented"""
    #     for func in self.__funcs:
    #         with self.subTest("undocumented function", function=func):
    #             self.assertIsNot(func[1].__doc__, None,
    #                              "{:s} is not documented".format(func[0]))
    #             self.assertTrue(len(func[1].__doc__) > 1,
    #                             "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the Place class is documented"""
        self.assertIsNot(Place.__doc__, None,
                         "Place is not documented")
        self.assertTrue(len(Place.__doc__) > 1,
                        "Place is not documented")

    def test_module_docs(self):
        """ Tests if place.py is documented"""
        self.assertIsNot(place.__doc__, None,
                         "place.py is not documented")
        self.assertIsNot(len(place.__doc__) > 1,
                         "place.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/place.py", "tests/test_models/test_place.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestPlace(unittest.TestCase):
    """ Tests for the Place class"""
    def test_subclass(self):
        """ tests if the Place class is inheriting from the BaseModel class"""
        inst = Place()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_attrs(self):  # add test for attribute "types"
        """ tests if the Place instance has all the necessary attributes"""
        inst = Place()
        with self.subTest(attribute="city_id"):
            self.assertTrue(hasattr(inst, "city_id"))
            self.assertEqual(inst.city_id, "")
        with self.subTest(attribute="user_id"):
            self.assertTrue(hasattr(inst, "user_id"))
            self.assertEqual(inst.user_id, "")
        with self.subTest(attribute="name"):
            self.assertTrue(hasattr(inst, "name"))
            self.assertEqual(inst.name, "")
        with self.subTest(attribute="description"):
            self.assertTrue(hasattr(inst, "description"))
            self.assertEqual(inst.description, "")
        with self.subTest(attribute="number_rooms"):
            self.assertTrue(hasattr(inst, "number_rooms"))
            self.assertEqual(inst.number_rooms, 0)
        with self.subTest(attribute="number_bathrooms"):
            self.assertTrue(hasattr(inst, "number_bathrooms"))
            self.assertEqual(inst.number_bathrooms, 0)
        with self.subTest(attribute="max_guest"):
            self.assertTrue(hasattr(inst, "max_guest"))
            self.assertEqual(inst.max_guest, 0)
        with self.subTest(attribute="price_by_night"):
            self.assertTrue(hasattr(inst, "price_by_night"))
            self.assertEqual(inst.price_by_night, 0)
        with self.subTest(attribute="latitude"):
            self.assertTrue(hasattr(inst, "latitude"))
            self.assertEqual(inst.latitude, 0)
        with self.subTest(attribute="longitude"):
            self.assertTrue(hasattr(inst, "longitude"))
            self.assertEqual(inst.longitude, 0)
        with self.subTest(attribute="amenity_ids"):
            self.assertTrue(hasattr(inst, "amenity_ids"))
            self.assertEqual(inst.amenity_ids, [])

    def test_str(self):
        """ Tests if the str method returns the correct format"""
        inst = Place()
        string = "[Place] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
