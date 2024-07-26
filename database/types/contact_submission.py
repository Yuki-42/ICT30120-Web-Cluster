"""
Contains the ContactSubmission class.
"""
# Standard Library Imports
from datetime import datetime
from sqlite3 import Connection, Cursor, Row

# Third Party Imports

# Local Imports
from .base_type import BaseType

# Constants
__all__ = [
    "ContactSubmission"
]


class ContactSubmission(BaseType):
    """
    Represents a contact form submission.
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
            FROM contact_requests
            WHERE id = ?
            """,
            (self._id,)
        )
        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

    @property
    def email(self) -> str:
        """
        Gets the email.

        Returns:
            str: Email
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT email
            FROM contact_requests
            WHERE id = ?
            """,
            (self._id,)
        )
        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

    @property
    def phone(self) -> str | None:
        """
        Gets the phone.

        Returns:
            str: Phone
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT phone
            FROM contact_requests
            WHERE id = ?
            """,
            (self._id,)
        )

        data: tuple[str] = cursor.fetchone()
        cursor.close()

        # Return None if data is None
        if data is None:
            return None

        return data[0]

    @property
    def subject(self) -> str:
        """
        Gets the subject.

        Returns:
            str: Subject
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT subject
            FROM contact_requests
            WHERE id = ?
            """,
            (self._id,)
        )

        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

    @property
    def message(self) -> str:
        """
        Gets the message.

        Returns:
            str: Message
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT message
            FROM contact_requests
            WHERE id = ?
            """,
            (self._id,)
        )
        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

    @property
    def state(self) -> str:
        """
        Gets the state.

        Returns:
            str: State
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT state
            FROM contact_requests
            WHERE id = ?
            """,
            (self._id,)
        )
        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]

    @property
    def contact_method(self) -> str:
        """
        Gets the contact method.

        Returns:
            str: Contact method
        """
        cursor: Cursor = self._connection.cursor()
        cursor.execute(
            """
            SELECT contact_method
            FROM contact_requests
            WHERE id = ?
            """,
            (self._id,)
        )
        data: tuple[str] = cursor.fetchone()
        cursor.close()
        return data[0]
