import hashlib
import secrets


class InvalidCredentialsError(Exception):
    pass


_users: dict[str, str] = {}


def register(username: str, password: str) -> None:
    _users[username] = hashlib.sha256(password.encode()).hexdigest()


def login(username: str, password: str) -> str:
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username not in _users or _users[username] != hashed:
        raise InvalidCredentialsError("Invalid username or password.")
    return secrets.token_hex(32)
