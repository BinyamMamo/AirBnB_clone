#!/usr/bin/python3
"""
This module contains a class that serves as a base for
other classes in this package
"""


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
        print(self.to_dict())


    def save(self):
        """ saves this instance to storage"""
        self.updated_at = datetime.utcnow()
        # storage.new(self)
        # storage.save()

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

bm = BaseModel(name="Bini", age=20, created_at="2017-09-28T21:03:54.052298")
print("-----------")
b = BaseModel()
print("-----------")
