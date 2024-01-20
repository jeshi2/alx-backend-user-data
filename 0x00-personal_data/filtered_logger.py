#!/usr/bin/env python3
"""
filtered_logger module
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscate specified fields in a log message.
    """
    return re.sub(
        r'(' +
        '|'.join(fields) +
        r')=.*?' +
        re.escape(separator),
        r'\1=' +
        redaction +
        separator,
        message)
