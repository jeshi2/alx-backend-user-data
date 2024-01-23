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
        Split the decoded value based on the first colon
        """
        credentials = decoded_base64_authorization_header.split(':', 1)

        """
        Check if there are two parts in the credentials
        """
        if len(credentials) != 2:
            return None, None

        """
        Return user email and password
        """
        return credentials[0], credentials[1]

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

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User method
        """
        if request is None:
            return None

        """
        Extract the Authorization header
        """
        authorization_header = request.headers.get('Authorization')

        """
        Extract the Base64 part of the Authorization header
        """
        base64_authorization = self.extract_base64_authorization_header(
            authorization_header)

        """
        Decode the Base64 string
        """
        decoded_value = self.decode_base64_authorization_header(
            base64_authorization)

        """
        Extract user credentials from the decoded value
        """
        user_email, user_pwd = self.extract_user_credentials(decoded_value)

        """
        Retrieve the User instance from the credentials
        """
        user = self.user_object_from_credentials(user_email, user_pwd)

        return user
