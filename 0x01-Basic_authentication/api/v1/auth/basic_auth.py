#!/usr/bin/env python3
""" Basic Auth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract Base64 Authorization Header method
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        """
        Extract the Base64 part after "Basic "
        """
        base64_part = authorization_header.replace("Basic ", "", 1)
        return base64_part
