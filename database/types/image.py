"""
Contains the ImageForm class.
"""
# Standard Library Imports
from datetime import datetime

# Third Party Imports
from sqlite3 import Connection, Cursor, Row

# Local Imports
from .base_type import BaseType

# Constants
__all__ = [
    "Image"
]


class Image(BaseType):
    """
    Represents an image.
    """

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

    @property
    def dict(self) -> dict:
        """
        Gets the dictionary representation.

        Returns:
            dict: Dictionary representation
        """
        return {
            "id": self._id,
            "created_at": self._created_at.isoformat(),
            "name": self.name,
            "path": self.path,
            "description": self.description
        }
