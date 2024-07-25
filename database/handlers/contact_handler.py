"""
Contains the ContactHandler class.
"""
# Standard Library Imports
from datetime import datetime

# Third Party Imports
from sqlite3 import Connection, Cursor, Row

# Local Imports
from .base_handler import BaseHandler
from ..types.contact_submission import ContactSubmission

# Constants
__all__ = [
    "ContactHandler"
]


class ContactHandler(BaseHandler):
    """
    Handles interactions with the contact_requests table.
    """

    @property
    def all(self) -> list[ContactSubmission]:
        """
        Gets all contact requests.

        Returns:
            list[ContactSubmission]: Contact requests
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM contact_requests")
        data: list = [ContactSubmission(self._connection, row) for row in cursor.fetchall()]
        cursor.close()
        return data

    def new(
            self,
            name: str,
            email: str,
            subject: str,
            message: str,
            state: str,
            contact_method: str,
            phone: str = None
    ) -> None:
        """
        Creates a new contact request.

        Args:
            name (str): Name
            email (str): Email
            subject (str): Subject
            message (str): Message
            state (str): State
            contact_method (str): Preferred contact method
            phone (str): Phone number
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO contact_requests (name, email, phone, subject, message, state, contact_method) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (name, email, phone, subject, message, state, contact_method)
        )

        self._connection.commit()
        cursor.close()

    def get(
            self,
            id: str
    ) -> ContactSubmission:
        """
        Gets a contact request by id.

        Args:
            id (str): ID

        Returns:
            ContactSubmission: Contact request
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT *
            FROM contact_requests
            WHERE id = ?
            """,
            (id,)
        )

        data: Row = cursor.fetchone()

        return ContactSubmission(self._connection, data)
