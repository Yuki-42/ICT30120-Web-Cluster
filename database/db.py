"""
Simple database handler for email contact form submissions.
"""

# Standard Library Imports

# Third Party Imports
from sqlite3 import Connection, Cursor, connect

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

        # Check if the database is empty
        cursor: Cursor = self._connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables: list[tuple] = cursor.fetchall()
        cursor.close()

        if len(tables) != 4:
            # Create all tables
            cursor = self._connection.cursor()
            cursor.execute(
                """
                CREATE TABLE contact_requests
                (
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    name       TEXT NOT NULL,
                    email      TEXT NOT NULL,
                    phone      TEXT,
                    subject    TEXT NOT NULL,
                    message    TEXT NOT NULL,
                    state      TEXT NOT NULL,
                    contact_method TEXT NOT NULL
                );
                
                CREATE TABLE images
                (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    name        TEXT NOT NULL,
                    path        TEXT NOT NULL,
                    description TEXT NOT NULL
                );
                """
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
        