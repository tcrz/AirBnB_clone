#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel():
    """Base Model"""
    def __init__(self, *args, **kwargs):
        """initialize instance of BaseModel class"""
        if kwargs:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'created_at':
                    self.created_at = datetime.strptime(v,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if k == 'updated_at':
                    self.updated_at = datetime.strptime(v,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """class object represented as a string"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute 'updated_at'
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict.update({'created_at': obj_dict['created_at'].isoformat()})
        obj_dict.update({'updated_at': obj_dict['updated_at'].isoformat()})
        return obj_dict
