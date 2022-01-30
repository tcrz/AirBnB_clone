#!/usr/bin/python3
"""this is the init file"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
