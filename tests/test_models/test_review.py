#!/usr/bin/python3

import inspect
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from models.review import Review
from models import review
from unittest import mock


class TestReviewDocs(unittest.TestCase):
    """ Tests the Review class for documentation and style"""

    # __funcs = inspect.getmembers(Review, predicate=inspect.isfunction)

    # def test_func_docs(self):
    #     """ Tests if all methods of Review are documented"""
    #     for func in self.__funcs:
    #         with self.subTest("undocumented function", function=func):
    #             self.assertIsNot(func[1].__doc__, None,
    #                              "{:s} is not documented".format(func[0]))
    #             self.assertTrue(len(func[1].__doc__) > 1,
    #                             "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the Review class is documented"""
        self.assertIsNot(Review.__doc__, None,
                         "Review is not documented")
        self.assertTrue(len(Review.__doc__) > 1,
                        "Review is not documented")

    def test_module_docs(self):
        """ Tests if review.py is documented"""
        self.assertIsNot(review.__doc__, None,
                         "review.py is not documented")
        self.assertIsNot(len(review.__doc__) > 1,
                         "review.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/review.py", "tests/test_models/test_review.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestReview(unittest.TestCase):
    """ Tests for the Review class"""
    def test_subclass(self):
        """ tests if the Review class is inheriting from the BaseModel class"""
        inst = Review()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_attrs(self):
        """ tests if the Review instance has all the necessary attributes"""
        inst = Review()
        with self.subTest(attribute="place_id"):
            self.assertTrue(hasattr(inst, "place_id"))
            self.assertEqual(inst.place_id, "")
        with self.subTest(attribute="user_id"):
            self.assertTrue(hasattr(inst, "user_id"))
            self.assertEqual(inst.user_id, "")
        with self.subTest(attribute="text"):
            self.assertTrue(hasattr(inst, "text"))
            self.assertEqual(inst.text, "")

    def test_str(self):
        """ Tests if the str method returns the correct format"""
        inst = Review()
        string = "[Review] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
