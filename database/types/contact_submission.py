"""
Contains the ContactSubmission class.
"""
# Standard Library Imports
from datetime import datetime

# Third Party Imports
from sqlite3 import Connection, Cursor, Row

# Local Imports

# Constants
__all__ = [
    "ContactSubmission"
]


class ContactSubmission:
    """
    Represents a contact form submission.
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
        Initializes the contact form submission.

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
