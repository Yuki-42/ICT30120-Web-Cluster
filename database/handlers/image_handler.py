"""
Contains the ImageHandler class.
"""
# Standard Library Imports
from sqlite3 import Cursor, Row

# Third Party Imports

# Local Imports
from .base_handler import BaseHandler
from ..types.image import Image

# Constants
__all__ = [
    "ImageHandler"
]


class ImageHandler(BaseHandler):
    """
    Handles interactions with the images table.
    """

    @property
    def all(self) -> list[Image]:
        """
        Gets all images.

        Returns:
            list[Image]: Images requests
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM images")
        data: list = [Image(self._connection, row) for row in cursor.fetchall()]
        cursor.close()
        return data

    def new(
            self,
            name: str,
            path: str,
            description: str
    ) -> None:
        """
        Creates a new image.

        Args:
            name (str): Name
            path (str): Path
            description (str): Description
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO images (name, path, description) VALUES (?, ?, ?)",
            (name, path, description)
        )

        self._connection.commit()
        cursor.close()

    def get(
            self,
            id: str
    ) -> Image:
        """
        Gets an image.

        Args:
            id (str): ID

        Returns:
            Image: Image
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM images
            WHERE id = ?
            """,
            (id,)
        )

        data: Row = cursor.fetchone()

        return Image(self._connection, data)
