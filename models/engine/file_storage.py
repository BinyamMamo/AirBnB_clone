#!/usr/bin/python3
"""
stores a dictionary object to a json file
"""

import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ basic class for storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):  # to be edited
        """ returns the objects dictionary"""
        return self.__objects

    def new(self, obj):  # more of set(self, obj) adds an inst
        """ stores the object in a dictionary"""

        if (obj is not None):
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ serializes the stored objects and saves them to json file"""

        output = {}

        for key, obj in self.__objects.items():
            output[key] = obj.to_dict()

        with open(self.__file_path, 'w') as jsonfile:
            json.dump(output, jsonfile)  # indent=4

    def reload(self):
        """ loads objects from the json file storage"""

        __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        try:
            with open(self.__file_path, 'r') as jsonfile:
                objs = json.load(jsonfile)
            for key, obj in objs.items():
                __class_name = obj["__class__"]
                __class = __classes[__class_name]
                self.__objects[key] = __class(**obj)
        except Exception:
            pass
