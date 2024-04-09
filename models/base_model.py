#!/usr/bin/python3
""" BaseModel class """
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Represents the BaseModel class of the HBnB project
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method\
        that initializes the new BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__.update({k: datetime.strptime(v, t_format)})
                elif k != "__class__":
                    self.__dict__.update({k: v})
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return the str representation\
        of the BaseModel instance
        """
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """
        Update updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance
        """
        new_dic = self.__dict__.copy()
        new_dic['__class__'] = self.__class__.__name__
        new_dic.update({'created_at': self.created_at.isoformat()})
        new_dic.update({'updated_at': self.updated_at.isoformat()})
        return new_dic
