#!/usr/bin/python3

"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """
    A class of serializing and deserializing objects to and fro a json file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        adds objects to the storage/sets in  objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes objects to the json file(path: _file_path)
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deserializes  the json file into the objects dictionary(if it exists)
        """
        try:
            with open(self.__file_path, "r")as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
