#!/usr/bin/python3
"""
User class for managing user information.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user."""
    email: str = ""  # User's email address
    password: str = ""  # User's password
    first_name: str = ""  # User's first name
    last_name: str = ""  # User's last name
