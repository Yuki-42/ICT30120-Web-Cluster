"""
Contains the base type for all db tables.
"""

# Standard Library Imports
from datetime import datetime
from sqlite3 import Connection, Row

# Third Party Imports

# Local Imports

# Constants

__all__ = [
    "BaseType"
]


class BaseType:
    """
    Represents a base type for all db tables.
    """

    _connection: Connection
    _id: int
    _created_at: datetime

    def __init__(
            self,
            connection: Connection,
            row: Row
    ) -> None:
        """
        Initializes the base type.

        Args:
            connection (Connection): Connection
            row (Row): Database row
        """
        self._connection = connection

        self._id = row[0]
        self._created_at = datetime.fromisoformat(row[1])

    @property
    def id(self) -> int:
        """
        Gets the id.

        Returns:
            int: Id
        """
        return self._id

    @property
    def created_at(self) -> datetime:
        """
        Gets the created at.

        Returns:
            datetime: Created at
        """
        return self._created_at

