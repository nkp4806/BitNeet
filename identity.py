import json
import secrets
from pathlib import Path

IDENTITY_DIR = Path.home() / ".bitneet"
IDENTITY_FILE = IDENTITY_DIR / "identity.json"


def generate_id():
    return "BN-" + secrets.token_hex(4).upper()


def save_identity(identity):
    IDENTITY_DIR.mkdir(parents=True, exist_ok=True)

    with open(IDENTITY_FILE, "w") as file:
        json.dump(identity, file, indent=4)


def load_identity():
    if not IDENTITY_FILE.exists():
        return None

    with open(IDENTITY_FILE, "r") as file:
        return json.load(file)


def create_identity(username):
    identity = {
        "id": generate_id(),
        "username": username
    }

    save_identity(identity)

    return identity


def get_identity(username):
    identity = load_identity()

    if identity is None:
        identity = create_identity(username)

    return identity
