#!/usr/bin/python3
"""class review module for the airbnb project"""
from models.base_model.py import BaseModel


class Review(BaseModel):
    """
    contains state.id, user.id and a text string
    """
    place_id = ""
    user_id = ""
    text = ""
