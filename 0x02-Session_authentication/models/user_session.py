#!/usr/bin/env python3
"""
UserSession module
"""

from models.base import Base
from datetime import datetime
from sqlalchemy import Column, String, DateTime


class UserSession(Base):
    """
    UserSession class represents the storage of user sessions in the database.

    Attributes:
        user_id (str): The ID of the associated user.
        session_id (str): The unique identifier for the user session.
        created_at (DateTime): The timestamp indicating when the user session was created.

    """

    __tablename__ = 'user_sessions'

    user_id = Column(String(60), nullable=False)
    session_id = Column(String(60), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize a new UserSession instance.

        Args:
            *args (list): Variable length argument list.
            **kwargs (dict): Arbitrary keyword arguments.

        Keyword Args:
            user_id (str): The ID of the associated user.
            session_id (str): The unique identifier for the user session.

        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id', "")
        self.session_id = kwargs.get('session_id', "")
