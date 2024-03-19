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

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            obj_dict = {}
            for key, value in FileStorage.__objects.item():
                obj_dict[key] = value to_dict()
            json.dump(obj_dict, f)
