#!/usr/bin/python3
"""
This module contains a class that serves as a base for
other classes in this package
"""


from datetime import datetime
# from models.engine import storage # == from models import storage
import uuid


class BaseModel:
    """ contains methods basis for the city, place and amenity classes"""
    def __init__(self):
        """ initializes the BaseModel class"""
        self.id = str(uuid.uuid4())
        # datetime.today() & datetime.now() return current
        # "local" time not UTC: the universal time
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

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
        return ("[{}] ({}) {}\
                ".format(self.__class__.__name__, self.id, self.__dict__))
