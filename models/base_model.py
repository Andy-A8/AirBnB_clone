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
    return (updated_at)
