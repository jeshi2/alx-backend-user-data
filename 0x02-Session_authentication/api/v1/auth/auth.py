#!/usr/bin/env python3
""" Auth module
"""
from typing import List, TypeVar
from flask import request, current_app


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require Auth method
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        """
        Add a trailing slash to path if it doesn't have one
        """
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            """
            Handle wildcards at the end of excluded paths
            """
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            else:
                """
                Add a trailing slash to excluded_path if it doesn't have one
                """
                if not excluded_path.endswith('/'):
                    excluded_path += '/'

                if path == excluded_path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization Header method
        """
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User method
        """
        return None

    def session_cookie(self, request=None) -> str:
        """ Session Cookie method
        """
        if request is None:
            return None

        session_cookie_name = current_app.config.get(
            'SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_cookie_name)
