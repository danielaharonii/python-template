"""Module implementing a PostOffice message routing simulation."""


class PostOffice:
    """A Post Office class. Allows users to message each other."""

    def __init__(self, usernames: list[str]) -> None:
        """
        Initializes the PostOffice with a list of registered usernames.

        :param usernames: List of initial usernames.
        """
        self.message_id = 0
        self.boxes: dict[str, list[dict[str, object]]] = {
            user: [] for user in usernames
        }

    def send_message(
        self, sender: str, recipient: str, message_body: str, urgent: bool = False
    ) -> int:
        """
        Send a message to a recipient.

        :param sender: The message sender's username.
        :param recipient: The message recipient's username.
        :param message_body: The body of the message.
        :param urgent: The urgency of the message. Urgent messages appear first.
        :return: The message ID, auto-incremented number.
        :raises KeyError: If the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details: dict[str, object] = {
            "id": self.message_id,
            "body": message_body,
            "sender": sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(
        self, username: str, num_messages: int | None = None
    ) -> list[dict[str, object]]:
        """
        Reads and removes up to `num_messages` unread messages from `username`'s inbox.

        :param username: The inbox owner's username.
        :param num_messages: Number of messages to read; reads all if None.
        :return: List of read message dictionaries.
        :raises KeyError: If `username` does not exist.
        """
        inbox = self.boxes[username]
        if num_messages is not None and num_messages <= 0:
            return []
        if num_messages is None or num_messages >= len(inbox):
            read_messages = list(inbox)
            inbox.clear()
            return read_messages

        read_messages = inbox[:num_messages]
        del inbox[:num_messages]
        return read_messages

    def search_inbox(self, username: str, query: str) -> list[dict[str, object]]:
        """
        Searches `username`'s inbox for messages containing `query` without removing them.

        :param username: The inbox owner's username.
        :param query: Substring to search for in message bodies.
        :return: List of matching message dictionaries.
        :raises KeyError: If `username` does not exist.
        """
        return [
            message
            for message in self.boxes[username]
            if query in str(message["body"])
        ]


if __name__ == "__main__":
    office = PostOffice(["alice", "bob"])
    office.send_message("alice", "bob", "Hello Bob!")
    print(office.read_inbox("bob"))