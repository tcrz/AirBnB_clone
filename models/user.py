#!/usr/bin/python3
"""
User class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    # super().__init__()
