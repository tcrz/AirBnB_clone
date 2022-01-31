#!/usr/bin/python3
""" A module that serializes instances to a JSON file and deserializes JSON file to instances """

import json
from os.path import exists
from models.base_model import BaseModel

'''class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id 
            
            Args:
                obj: key value pair to be assigned
        """
        FileStorage.__objects[obj.__class__.__name__.id] = obj 

    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)
    
    def reload(self):
        """ deserializes the JSON file to __objects """

        file_exists = exists(FileStorage.__file_path)

        if file_exists:
            with open(file_exists, 'r') as f:
                data = json.load(f)
        else:
            pass'''
