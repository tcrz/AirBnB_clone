#!/usr/bin/python3
""" Module base other modules inherit from"""

import uuid
import datetime

class BaseModel():

    def __init__(self, *args, **kwargs):
        """ Base Init.

        Args:
            id: unique id of instance
            created_at: creation time of instance
            updated_at: modifcation time of the instance
        """
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.datetime.strptime(kwargs['created_at'],'%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'],'%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """return string representation of the object """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime 
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
