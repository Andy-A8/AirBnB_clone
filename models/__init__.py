#!/usr/bin/python3
"""
    Create a unique FileStorage instance for the application:
        Import FileStorage,
        Create the variable storage to be an instance of FileStorage,
        call reload on the created variable.
"""

from models.engine.file_storage import FileStorage

storage = Filestorage()
storage.reload()
