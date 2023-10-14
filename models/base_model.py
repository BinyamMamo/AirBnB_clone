#!/usr/bin/python3
"""
This module contains a class that serves as a base for
other classes in this package
"""

import models

from datetime import datetime
# from models.engine import storage # == from models import storage

import inspect
import json
import uuid

class BaseModel:
    """ contains methods basis for the city, place and amenity classes"""

    def __init__(self, *args, **kwargs):
        """ initializes the BaseModel class"""

        obj = {}

        new_inst = False
        # if (kwargs is None or kwargs["created_at"] is None
        # or type(kwargs["created_at"] is not datetime)):
        if (kwargs is None or kwargs["created_at"] is None):
                new_inst = True
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if (key != "__class__"):
                obj[key] = value
        new_obj = json.loads(json.dumps(obj))

        for key, value in new_obj.items():
            if (key == "updated_at" or key == "created_at"):
                value = datetime.strptime(str(value), "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)

        if (new_inst):
            print("new")
            models.storage.new(self)
        # print(self.to_dict())

    def save(self):
        """ saves this instance to storage"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)  # not sure if needed here
        models.storage.save()

        print(models.storage.all())

    def to_dict(self):
        """ converts this instance to a json format"""
        this_dict = {}
        this_dict["__class__"] = self.__class__.__name__
        self_dict = self.__dict__

        for key, value in self_dict.items():
            if (key == "updated_at" or key == "created_at"):
                # == value.date() + "T" + value.time()
                value = str(value.isoformat())
            this_dict[key] = value

        return this_dict

    def __str__(self):
        """ returns a string representation of this instance"""
        # return ("[{}] ({}) {}\
        #         ".format(self.__class__.__name__, self.id, self.__dict__))

