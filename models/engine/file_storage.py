#!/usr/bin/python3
"""Defines a class FileStorage"""

import json


class FileStorage:
    """Represents a storage engine

    Attributes:
        __file_path (string): The name of file and path to JSON file.
        __object (dictionary): A dictionary to store all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj
