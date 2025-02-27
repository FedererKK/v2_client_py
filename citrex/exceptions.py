"""
Exceptions for the citrex package.
"""


class UserInputValidationError(Exception):
    """
    Exception raised when a user input is invalid.
    """


class ClientError(Exception):
    """
    Exception raised when there is an error with the client.
    """
