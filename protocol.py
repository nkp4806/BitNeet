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

def validate(packet):
    if not isinstance(packet, dict):
        return False

    if packet.get("version") != PROTOCOL_VERSION:
        return False

    if packet.get("type") not in {"message", "join", "leave", "server"}:
        return False

    if "user" not in packet:
        return False

    if "message" not in packet:
        return False

    return True

class Decoder:
    def __init__(self):
        self.buffer = b""

    def feed(self,data):
        self.buffer += data

        packets = []

        while b"\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\n", 1)

            if line :
                packets.append(decode(line))

        return packets

def format_packet(packet):
    packet_type = packet.get("type")

    if packet_type == "message":
        return f"[{packet['user']}] {packet['message']}"

    if packet_type == "join":
        return f"[SERVER] {packet['user']} joined the chat."

    if packet_type == "leave":
        return f"[SERVER] {packet['user']} left the chat."

    if packet_type == "server":
        return f"[SERVER] {packet['message']}"

    return "[UNKNOWN] Invalid packet"
