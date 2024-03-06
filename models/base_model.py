#!/usr/bin/python3
"""Defines a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model of this project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel

        Args:
            *args: list of argumentsa (unused).
            **kwargs (dict): key/value pairs of attributes.
        """

        if kwargs and len(kwargs) is not o:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], %Y-%m-%dT%H:%M:%S.%f)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], %Y-%m-%dT%H:%M:%S.%f)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the pi attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all keys/values of__dict__of the instance:
            instance attributes: created_at and cupdated_at
            a key __class__ must be added with the class name of the object
            inst.attributes must be converted to string object in IOS format
        """

        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()

        return the_dict
