#!/usr/bin/env python3
""" Basic Auth module
"""
import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode Base64 Authorization Header method
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            """
            Decode the Base64 string
            """
            decoded_value = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return decoded_value
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract User Credentials method
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        """
        Check if the decoded value contains ":"
        """
        if ":" not in decoded_base64_authorization_header:
            return None, None

        """
        Split the decoded value into email and password
        """
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password
