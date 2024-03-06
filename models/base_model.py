#!/usr/bin/python3
"""Defines a class BaseModel"""

import uuid


class BaseModel:
    """Represents the base model of this project"""

    pass


def id(self):
    """Generate unique id using uuid4()"""
    self.id = str(uuid.uuid4())
    return (self.id)
