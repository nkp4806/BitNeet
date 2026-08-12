import json

PROTOCOL_VERSION = 1


def create_message(user, message):
    return {
        "version": PROTOCOL_VERSION,
        "type": "message",
        "user": user,
        "message": message
    }

def create_join(user):
    return{
        "version": PROTOCOL_VERSION,
        "type": "join",
        "user": user,
        "message": None
    }

def create_leave(user):
    return{
        "version": PROTOCOL_VERSION,
        "type": "leave",
        "user": user,
        "message": None
    }

def create_server(message):
    return {
        "version": PROTOCOL_VERSION,
        "type": "server",
        "user": "SERVER",
        "message": message
    }

def encode(packet):
    data = json.dumps(packet)
    return (data + "\n").encode()

def decode(data):
    data = data.decode().strip()
    return json.loads(data)


