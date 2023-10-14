#!/usr/bin/python3
"""
Creates a state model class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ class for state"""
    name: str = ""
