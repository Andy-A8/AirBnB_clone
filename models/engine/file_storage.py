#!/usr/bin/python3
"""Defines a class FileStorage"""
import json
from models.base_model import BaseModel


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
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON fileexists
            Otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised).
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in obj_dict.values():
                    c_name = o["__class__"]
                    del o["__class"]
                    self.new(eval(c_name)(**o))
        except FileNotFoundError:
            return
