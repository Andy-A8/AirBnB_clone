#!/usr/bin/python3
"""Defines a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of this project"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all keys/values of__dict__of the instance:
            instance attributes: created_at and cupdated_at
            a key __class__ must be added with the class name of the object
            inst.attributes must be converted to string object in IOS format
        """
        d_dict = self.__dict__.copy()
        d_dict["created_at"] = self.created_at.isoformat()
        d_dict["updated_at"] = self.updated_at.isoformat()
        d_dict["__class__"] = self.__class__.__name__
        return d_dict
