"""
Contains the ImageForm class.
"""
# Standard Library Imports
from datetime import datetime

# Third Party Imports
from sqlite3 import Connection, Cursor, Row

# Local Imports

# Constants
__all__ = [
    "Image"
]


class Image:
    """
    Represents an image.
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
        Initializes the imagen.

        Args:
            connection (Connection): Connection
            row (Row): Database row
        """
        self._connection = connection

        self._id = row["id"]
        self._created_at = datetime.fromisoformat(row["created_at"])

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

    @property
    def name(self) -> str:
        """
        Gets the name.

        Returns:
            str: Name
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT name
            FROM images
            WHERE id = ?
            """,
            (self._id,)
        )
        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

    @property
    def path(self) -> str:
        """
        Gets the path.

        Returns:
            str: Path
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT path
            FROM images
            WHERE id = ?
            """,
            (self._id,)
        )
        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

    @property
    def description(self) -> str:
        """
        Gets the description.

        Returns:
            str: Description
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT description
            FROM images
            WHERE id = ?
            """,
            (self._id,)
        )

        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

