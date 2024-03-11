#!/usr/bin/python3
"""Defines a User class"""
from models.base_model import BaseModel


class User(BaseMOdel):
    """Represents a User.

    Attributes:
    (all attributes are of string (str) data type and of the user)
            email: The email
            password: The password
            first_name: The first name
            last_name: The last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
