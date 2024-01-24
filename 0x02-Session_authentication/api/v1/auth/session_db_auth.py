#!/usr/bin/env python3
"""
SessionDBAuth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession

from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class
    """

    def create_session(self, user_id=None):
        """ Create a new session and store it in the database
        """
        session_id = super().create_session(user_id)
        if session_id:
            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return the User ID by requesting UserSession in the database
        """
        if session_id is None:
            return None

        user_session = UserSession.search({'session_id': session_id})
        if not user_session or not user_session[0].user_id:
            return None

        session_duration = self.session_duration

        if session_duration <= 0:
            return user_session[0].user_id

        created_at = user_session[0].created_at
        expiration_time = created_at + timedelta(seconds=session_duration)

        if expiration_time < datetime.utcnow():
            return None

        return user_session[0].user_id

    def destroy_session(self, request=None):
        """ Destroy the UserSession based on the Session ID from the request cookie
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        user_session = UserSession.search(
            {'session_id': session_id, 'user_id': user_id})

        if not user_session:
            return False

        user_session[0].delete()
        return True
