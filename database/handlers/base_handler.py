"""
Contains the BaseHandler class.
"""
# Standard Library Imports
from sqlite3 import Connection

# Third Party Imports

# Local Imports

# Constants
__all__ = [
    "BaseHandler"
]


class BaseHandler:
    """
    Base handler class.
    """

    _connection: Connection

    def __init__(
            self,
            connection: Connection
    ) -> None:
        """
        Initializes the base handler.

        Args:
            connection (Connection): Connection
        """
        self._connection = connection
