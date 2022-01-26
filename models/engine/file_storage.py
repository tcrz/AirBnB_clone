#!/usr/bin/python3
"""
File storage class
"""
import json
import os
from datetime import datetime


class FileStorage():
    """File Storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[obj_key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                obj_data = json.load(file)
                obj_data.update(FileStorage.__objects)
            with open(FileStorage.__file_path, mode='w') as file:
                json.dump(obj_data, file)
        else:
            with open(FileStorage.__file_path, mode='w') as file:
                json.dump(FileStorage.__objects, file, default=str)

    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                FileStorage.__objects = json.load(file)
                # print(FileStorage.__objects)
                # FileStorage.__objects['created_at'].update(datetime.strptime(
                #     FileStorage.__objects['created_at'], '%Y-%m-%dT%H:%M:%S.%f')) 
                # FileStorage.__objects['updated_at'].update(datetime.strptime(
                #     FileStorage.__objects['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'))
                