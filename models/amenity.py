#!/usr/bin/python3
"""
Creates a state model class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ base class for amenity"""
    name: str = ""
