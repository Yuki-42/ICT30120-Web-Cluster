"""
Simple database handler for email contact form submissions.
"""

# Standard Library Imports

# Third Party Imports
from sqlite3 import Connection, connect

# Local Imports
from .handlers import BaseHandler, ContactHandler, ImageHandler

# Constants
DB_PATH: str = "db.db"


class Database:
    """
    Handles connections to the database.
    """
    _connection: Connection
    _handlers: list[BaseHandler]

    def __init__(self) -> None:
        """
        Initializes the database.
        """
        self._connection = connect(
            DB_PATH,
            check_same_thread=False
        )
        self._handlers = [
            ContactHandler(self._connection),
            ImageHandler(self._connection)
        ]

    @property
    def contact_requests(self) -> ContactHandler:
        """
        Gets the contact requests handler.

        Returns:
            ContactHandler: Contact requests handler
        """
        # Inspection is disabled because the type hint is correct
        # noinspection PyTypeChecker
        return self._handlers[0]

    @property
    def images(self) -> ImageHandler:
        """
        Gets the images handler.

        Returns:
            ImageHandler: Images handler
        """
        # Inspection is disabled because the type hint is correct
        # noinspection PyTypeChecker
        return self._handlers[1]

    def close(self) -> None:
        """
        Closes the database connection.
        """
        self._connection.close()
        