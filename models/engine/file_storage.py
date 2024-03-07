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
