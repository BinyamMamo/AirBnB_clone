#!/usr/bin/python3

import inspect
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from models.state import State
from models import state
from unittest import mock


class TestStateDocs(unittest.TestCase):
    """ Tests the State class for documentation and style"""

    # __funcs = inspect.getmembers(State, predicate=inspect.isfunction)

    # def test_func_docs(self):
    #     """ Tests if all methods of State are documented"""
    #     for func in self.__funcs:
    #         with self.subTest("undocumented function", function=func):
    #             self.assertIsNot(func[1].__doc__, None,
    #                              "{:s} is not documented".format(func[0]))
    #             self.assertTrue(len(func[1].__doc__) > 1,
    #                             "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the State class is documented"""
        self.assertIsNot(State.__doc__, None,
                         "State is not documented")
        self.assertTrue(len(State.__doc__) > 1,
                        "State is not documented")

    def test_module_docs(self):
        """ Tests if state.py is documented"""
        self.assertIsNot(state.__doc__, None,
                         "state.py is not documented")
        self.assertIsNot(len(state.__doc__) > 1,
                         "state.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/state.py", "tests/test_models/test_state.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestState(unittest.TestCase):
    """ Tests for the State class"""
    def test_subclass(self):
        """ tests if the State class is inheriting from the BaseModel class"""
        inst = State()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_attrs(self):
        """ tests if the State instance has all the necessary attributes"""
        inst = State()
        with self.subTest(attribute="name"):
            self.assertTrue(hasattr(inst, "name"))
            self.assertEqual(inst.name, "")

    def test_str(self):
        """ Tests if the str method returns the correct format"""
        inst = State()
        string = "[State] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
