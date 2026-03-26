class InvalidRecipientError(Exception):
    pass


class InvalidMessageError(Exception):
    pass


def send_notification(email: str, message: str) -> bool:
    if not email:
        raise InvalidRecipientError("Recipient email cannot be empty.")
    if not message:
        raise InvalidMessageError("Message cannot be empty.")
    return True
