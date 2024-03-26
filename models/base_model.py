#!usr/bin/python3
"""This is  a module for defining the BaseModel for the airBnB Clone"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A basemodel for common attributes and methods
    """

    def __init__(self):
        """
        Initiliser for BaseModel class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """
        string representation of the basemodel object
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the the public instace attribute update_at with the current utc
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary representation of the basemodel
        object
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        for key, value in my_dict.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat
        return my_dict
