from models.base_model import BaseModel
"""class user that inherits from a BaseModel"""


class User(BaseModel):
    """
    User model class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
