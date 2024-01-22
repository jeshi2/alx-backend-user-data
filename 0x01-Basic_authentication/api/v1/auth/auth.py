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
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization Header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User method
        """
        return None
