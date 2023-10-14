#!/usr/bin/python3
"""
Creates a review model class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ class for review"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
