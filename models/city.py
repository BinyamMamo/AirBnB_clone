#!/usr/bin/python3
"""
Creates a state model class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ class for city"""
    state_id: str = ""
    name: str = ""
