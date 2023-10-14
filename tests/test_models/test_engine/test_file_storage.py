#!/usr/bin/python3

import inspect
import json
import unittest
import pycodestyle

from datetime import datetime as dt
from models import base_model
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine import file_storage


FileStorage = file_storage.FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """ Tests the FileStorage class for documentation and style"""

    __funcs = inspect.getmembers(FileStorage, predicate=inspect.isfunction)

    def test_func_docs(self):
        """ Tests if all methods of FileStorage are documented"""
        for func in self.__funcs:
            with self.subTest("undocumented function", function=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} is not documented".format(func[0]))
                self.assertTrue(len(func[1].__doc__) > 1,
                                "{:s} is not documented".format(func[0]))

    def test_class_docs(self):
        """ Tests if the FileStorage class is documented"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage is not documented")
        self.assertTrue(len(FileStorage.__doc__) > 1,
                        "FileStorage is not documented")

    def test_module_docs(self):
        """ Tests if file_storage.py is documented"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py is not documented")
        self.assertIsNot(len(file_storage.__doc__) > 1,
                         "file_storage.py is not documented")

    def test_pycodestyle(self):
        """ Tests if this module passes the pycodestyle checker"""
        for module in ["models/engine/file_storage.py",
                       "tests/test_models/test_engine/test_file_storage.py"]:
            with self.subTest("undocumented module", module=module):
                error = pycodestyle.Checker(module).check_all()
                self.assertEqual(error, 0)


class TestFileStorage(unittest.TestCase):
    """ Test the FileStorage class"""
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def test_all(self):
        """ Tests if all() returns the stored objects in a dictionary form"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """ Test that new adds an object to storage"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in self.__classes.items():
            with self.subTest(key=key, value=value):
                inst = value()
                inst_key = inst.__class__.__name__ + "." + inst.id
                storage.new(inst)
                test_dict[inst_key] = inst
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """ Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in self.__classes.items():
            inst = value()
            inst_key = inst.__class__.__name__ + "." + inst.id
            new_dict[inst_key] = inst
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
