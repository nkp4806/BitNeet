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

original = create_message("neet", "hello")

encoded = encode(original)
decoded = decode(encoded)

print("original:", original)
print("encoded:", encoded)
print("decoded:", decoded)

if original == decoded:
    print("protocol test passed!")
else:
    print("protocol test failed!")
