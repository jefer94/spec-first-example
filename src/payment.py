import uuid


class InvalidAmountError(Exception):
    pass


def process_payment(amount: float, card_token: str) -> str:
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero.")
    return str(uuid.uuid4())
