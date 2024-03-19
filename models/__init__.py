#!/usr/bin/python3
"""Create a unique FileStorage instance for your application:
        Import file_storage.py
        Create the variable storage, an instance of FileStorage
        Call reload() method on this variable
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
