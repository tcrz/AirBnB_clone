#!/usr/bin/python3
"""
User class that inherits from BaseModel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """User Class"""
    def __init__(self):
        """initializing User instance"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
