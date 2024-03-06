#!/usr/bin/python3
"""Defines a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model of this project"""

    pass


def id(self):
    """Generate unique id using uuid4()"""
    self.id = str(uuid.uuid4())
    return (self.id)


def created_at(self):
    """Generates the current datetime when an instance is created"""
    self.created_at = datetime.today
    return (self.created_at)


def updated_at(self):
    """Generates the current updated datetime every time object is changed"""
    self.updated_at = datetime.today
    return (self.updated_at)


def __str__(self):
    """Returns string representation of BaseModel instance"""
    return "[{}] ({}) {}".format(self.__class__.__name__,
                                 self.id, self.__dict__)


def save(self):
    """Updates the pi attribute updated_at with the current datetime"""
    self.updated_at = datetime.today()
    return (self.updated_at)
