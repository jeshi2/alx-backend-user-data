#!/usr/bin/env python3
""" Basic Auth module
"""
import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


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

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ User Object from Credentials method
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        """
        Search for the user in the database based on email
        """
        users = User.search({'email': user_email})
        if not users:
            return None

        """
        Retrieve the first user (assuming email is unique)
        """
        user = users[0]

        """
        Check if the provided password is valid
        """
        if not user.is_valid_password(user_pwd):
            return None

        return user
