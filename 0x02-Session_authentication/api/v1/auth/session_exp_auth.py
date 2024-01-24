#!/usr/bin/env python3

"""
Session Expiration
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """ Session with Expiration Auth class
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()

        # Assign session_duration attribute
        session_duration = os.getenv('SESSION_DURATION')
        try:
            self.session_duration = int(
                session_duration) if session_duration else 0
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Create Session ID method
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dict = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ User ID for Session ID method with expiration
        """
        if session_id is None or session_id not in self.user_id_by_session_id:
            return None

        session_dict = self.user_id_by_session_id[session_id]

        if self.session_duration <= 0:
            return session_dict['user_id']

        if 'created_at' not in session_dict:
            return None

        expiration_time = session_dict['created_at'] + \
            timedelta(seconds=self.session_duration)

        if datetime.now() > expiration_time:
            return None

        return session_dict['user_id']
