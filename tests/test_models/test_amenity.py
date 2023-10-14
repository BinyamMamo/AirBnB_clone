#!/usr/bin/python3

import inspect
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from models.amenity import Amenity
from models import amenity
from unittest import mock


class TestAmenityDocs(unittest.TestCase):
    """ Tests the Amenity class for documentation and style"""

    # __funcs = inspect.getmembers(Amenity, predicate=inspect.isfunction)

    # def test_func_docs(self):
    #     """ Tests if all methods of Amenity are documented"""
    #     for func in self.__funcs:
    #         with self.subTest("undocumented function", function=func):
    #             self.assertIsNot(func[1].__doc__, None,
    #                              "{:s} is not documented".format(func[0]))
    #             self.assertTrue(len(func[1].__doc__) > 1,
    #                             "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the Amenity class is documented"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity is not documented")
        self.assertTrue(len(Amenity.__doc__) > 1,
                        "Amenity is not documented")

    def test_module_docs(self):
        """ Tests if amenity.py is documented"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py is not documented")
        self.assertIsNot(len(amenity.__doc__) > 1,
                         "amenity.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/amenity.py",
                       "tests/test_models/test_amenity.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestAmenity(unittest.TestCase):
    """ Tests for the Amenity class"""
    def test_subclass(self):
        """ tests if the Amenity class is inheriting from BaseModel"""
        inst = Amenity()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_attrs(self):
        """ tests if the Amenity instance has all the necessary attributes"""
        inst = Amenity()
        with self.subTest(attribute="name"):
            self.assertTrue(hasattr(inst, "name"))
            self.assertEqual(inst.name, "")

    def test_str(self):
        """ Tests if the str method returns the correct format"""
        inst = Amenity()
        string = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
