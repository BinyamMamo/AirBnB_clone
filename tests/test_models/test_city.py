#!/usr/bin/python3

import inspect
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from models.city import City
from models import city
from unittest import mock


class TestCityDocs(unittest.TestCase):
    """ Tests the City class for documentation and style"""

    # __funcs = inspect.getmembers(City, predicate=inspect.isfunction)

    # def test_func_docs(self):
    #     """ Tests if all methods of City are documented"""
    #     for func in self.__funcs:
    #         with self.subTest("undocumented function", function=func):
    #             self.assertIsNot(func[1].__doc__, None,
    #                              "{:s} is not documented".format(func[0]))
    #             self.assertTrue(len(func[1].__doc__) > 1,
    #                             "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the City class is documented"""
        self.assertIsNot(City.__doc__, None,
                         "City is not documented")
        self.assertTrue(len(City.__doc__) > 1,
                        "City is not documented")

    def test_module_docs(self):
        """ Tests if city.py is documented"""
        self.assertIsNot(city.__doc__, None,
                         "city.py is not documented")
        self.assertIsNot(len(city.__doc__) > 1,
                         "city.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/city.py", "tests/test_models/test_city.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestCity(unittest.TestCase):
    """ Tests for the city class"""
    def test_subclass(self):
        """ tests if the City class is inheriting from the BaseModel class"""
        inst = City()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_attrs(self):
        """ tests if the city instance has all the necessary attributes"""
        inst = City()
        with self.subTest(attribute="state_id"):
            self.assertTrue(hasattr(inst, "state_id"))
            self.assertEqual(inst.state_id, "")
        with self.subTest(attribute="name"):
            self.assertTrue(hasattr(inst, "name"))
            self.assertEqual(inst.name, "")

    def test_str(self):
        """ Tests if the str method returns the correct format"""
        inst = City()
        string = "[City] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
