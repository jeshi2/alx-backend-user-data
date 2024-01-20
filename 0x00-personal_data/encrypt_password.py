#!/usr/bin/env python3
"""
Hashing
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with salt.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
