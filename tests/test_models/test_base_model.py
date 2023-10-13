#!/usr/bin/python3

import inspect
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from unittest import mock


class TestBaseModelDocs(unittest.TestCase):
    """ Tests the BaseModel class for documentation and style"""

    __funcs = inspect.getmembers(BaseModel, predicate=inspect.isfunction)

    def test_func_docs(self):
        """ Tests if all methods of BaseModel are documented"""
        for func in self.__funcs:
            with self.subTest("undocumented function", function=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} is not documented".format(func[0]))
                self.assertTrue(len(func[1].__doc__) > 1,
                                "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the BaseModel class is documented"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel is not documented")
        self.assertTrue(len(BaseModel.__doc__) > 1,
                        "BaseModel is not documented")

    def test_module_docs(self):
        """ Tests if base_model.py is documented"""
        self.assertIsNot(base_model.__doc__, None,
                         "base_model.py is not documented")
        self.assertIsNot(len(base_model.__doc__) > 1,
                         "base_model.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/base_model.py",
                       "tests/test_models/test_base_model.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """ Tests if the __init__ method is working as it should"""
        inst = BaseModel()
        inst.name = "My_First_Model"
        inst.my_number = 89
        self.assertIs(type(inst), BaseModel)
        
        attrs = {
            "id": str,
            "created_at": dt,
            "updated_at": dt  # name, my_number
        }

        self.assertEqual(inst.name, "My_First_Model")
        self.assertEqual(inst.my_number, 89)

        for attr, atype in attrs.items():
            with self.subTest("attribute type"):
                self.assertIn(attr, inst.__dict__, "attribute not found")
                self.assertIs(type(inst.__dict__[attr]), atype, "attribute type does not match")  # inappropriate attribite type


    # def test_dt_attr(self):
    #     """ Tests if updated_at and created_at are working well"""
    #     inst = BaseModel()
    #     self.assertEqual(inst.created_at, inst.updated_at)

            