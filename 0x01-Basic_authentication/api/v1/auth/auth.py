#!/usr/bin/env python3
""" Auth module
"""
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User method
        """
        return None
