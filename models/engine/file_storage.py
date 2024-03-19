#!/usr/bin/python3
"""Defines a class FileStorage"""


class FileStorage:
    """Represents a storage engine.

    Attributes:
        __file_path (str): The file name to save objects.
        __objects (dict): A dictionary of objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
