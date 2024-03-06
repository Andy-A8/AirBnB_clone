#!/usr/bin/python3
"""Defines a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model of this project"""

    pass


def __init__(self, id, created_at, updated_at):
    """Generate unique id using uuid4()

    Args:
        id = unique id.
        created_at = current datetime of created instance.
        Updated_at = Current datetime every time an instance is updated.
    """

    self.id = str(uuid.uuid4())
    self.created_at = datetime.today
    self.updated_at = datetime.today


def __str__(self):
    """Returns string representation of BaseModel instance"""
    return "[{}] ({}) {}".format(self.__class__.__name__
                                 self.id, self.__dict__)


def save(self):
    """Updates the pi attribute updated_at with the current datetime"""
    self.updated_at = datetime.now()
    return (self.updated_at)


def to_dict(self):
    """Returns a dictionary with all keys/values of__dict__of the instance:
        instance attributes: created_at and cupdated_at
        a key __class__ must be added with the class name of the object
        instance attributes must be converted to string object in IOS format.
    """

    the_dict = self.__dict__.copy()
    the_dict["__class__"] = self.__class__.__name__
    the_dict["created_at"] = self.created_at.isoformat()
    the_dict["updated_at"] = self.updated_at.isoformat()

    return the_dict
