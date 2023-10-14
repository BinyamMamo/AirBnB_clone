#!/usr/bin/python3

import inspect
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from models.user import User
from models import user
from unittest import mock


class TestUserDocs(unittest.TestCase):
    """ Tests the User class for documentation and style"""

    # __funcs = inspect.getmembers(User, predicate=inspect.isfunction)

    # def test_func_docs(self):
    #     """ Tests if all methods of User are documented"""
    #     for func in self.__funcs:
    #         with self.subTest("undocumented function", function=func):
    #             self.assertIsNot(func[1].__doc__, None,
    #                              "{:s} is not documented".format(func[0]))
    #             self.assertTrue(len(func[1].__doc__) > 1,
    #                             "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the User class is documented"""
        self.assertIsNot(User.__doc__, None,
                         "User is not documented")
        self.assertTrue(len(User.__doc__) > 1,
                        "User is not documented")

    def test_module_docs(self):
        """ Tests if user.py is documented"""
        self.assertIsNot(user.__doc__, None,
                         "user.py is not documented")
        self.assertIsNot(len(user.__doc__) > 1,
                         "user.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/user.py", "tests/test_models/test_user.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestUser(unittest.TestCase):
    """ Tests for the user class"""
    def test_subclass(self):
        """ tests if the User class is inheriting from the BaseModel class"""
        inst = User()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_attrs(self):
        """ tests if the user instance has all the necessary attributes"""
        inst = User()
        with self.subTest(attribute="email"):
            self.assertTrue(hasattr(inst, "email"))
            self.assertEqual(inst.email, "")
        with self.subTest(attribute="password"):
            self.assertTrue(hasattr(inst, "password"))
            self.assertEqual(inst.password, "")
        with self.subTest(attribute="first_name"):
            self.assertTrue(hasattr(inst, "first_name"))
            self.assertEqual(inst.first_name, "")
        with self.subTest(attribute="last_name"):
            self.assertTrue(hasattr(inst, "last_name"))
            self.assertEqual(inst.last_name, "")

    def test_str(self):
        """ Tests if the str method returns the correct format"""
        inst = User()
        string = "[User] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
