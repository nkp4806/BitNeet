import socket
import threading
import protocol

HOST = "0.0.0.0"
PORT = 4806

clients = []
users = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print(f"Server started on port {PORT}")

def broadcast(message, sender):
    for client in clients.copy():
        if client != sender:
            try:
                client.send(message)
            except (ConnectionResetError, BrokenPipeError, OSError):
                if client in clients:
                    clients.remove(client)

def handle(client):
    decoder = protocol.Decoder()
    username = None
    user_id = None

    while True:
        try:
            data = client.recv(1024)

            if not data:
                break

            packets = decoder.feed(data)

            for packet in packets:
                if not protocol.validate(packet):
                    continue
                
                if packet["type"] == "join":
                    user_id = packet["id"]
                    username = packet["user"]

                    users[user_id] = {
                        "username": username,
                        "client": client
                    }

                    join_message = protocol.create_server(
                        f"{username} joined the chat."
                    )

                    broadcast(protocol.encode(join_message), client)

                elif packet["type"] == "leave":
                    leave_message = protocol.create_server(
                        f"{username} left the chat."
                    )

                    broadcast(protocol.encode(leave_message), client)

                    if user_id in users:
                        del users[user_id]

                    username = None
                    user_id = None
                    break

                else:
                    broadcast(protocol.encode(packet), client)

        except (ConnectionResetError, BrokenPipeError, OSError):
            break

    if username:
        leave_message = protocol.create_server(
            f"{username} left the chat."
        )

        broadcast(protocol.encode(leave_message), client)

    if user_id in users:
        del users[user_id]

    if client in clients:
        clients.remove(client)

    client.close()

try:
    while True:
        client, addr = server.accept()

        print(f"{addr} connected")

        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,), daemon=True)
        thread.start()

except KeyboardInterrupt:
    print("\nServer shutting down...")

finally:
    for client in clients:
        client.close()

    server.close()