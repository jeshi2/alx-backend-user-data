#!/usr/bin/env python3
"""
UserSession module
"""
from models.base import Base
from datetime import datetime
from sqlalchemy import Column, String, DateTime


class UserSession(Base):
    """
    UserSession class represents the UserSession model.

    Attributes:
    - user_id: A string representing the user ID.
    - session_id: A string representing the session ID.
    - created_at: A datetime object representing the creation timestamp.
    """

    __tablename__ = 'user_sessions'

    user_id = Column(String(60), nullable=False)
    session_id = Column(String(60), nullable=False)
    # created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize UserSession instance """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id', "")
        self.session_id = kwargs.get('session_id', "")")
