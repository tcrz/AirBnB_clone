#!/usr/bin/python3
""" Module base other modules inherit from"""

import uuid
import datetime
import json

def __init__(id, created_at, updated_at):
    """ Base Init.

        Args:
            id: unique id of instance
            created_at: creation time of instance
            updated_at: modifcation time of the instance
    """
    self.id = str(uuid.uuid4())
    self.created_at = datetime.datetime.now()
    self.updated_at = datetime.datetime.now()

def __str__(self):
    """return string representation of the object """
    return "[{}] ({}) {}".format(
            self.__class.__name__, self.id, self.__dict__)

def save(self):
    """ updates the public instance attribute updated_at with the
    current datetime 
    """

    self.updated_at = datetime.datetime.now()

def to_dict(self):
    """ returns a dictionary containing all keys/values of the instance """
    self.__dict__['__class__'] = self.__class.__name__
    self.__dict__['created_at'] = datetime.isofromat(self.created_at)
    self.__dict__['updated_at'] = datetime.isofromat(self.updated_at)
    return self.__dict__


