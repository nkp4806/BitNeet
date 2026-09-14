import socket
import threading
import protocol

HOST = "0.0.0.0"
PORT = 4806

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print(f"Server started on port {PORT}")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle(client):
    decoder = protocol.Decoder()
    username = None

    while True:
        try:
            data = client.recv(1024)

            if not data:
                break

            packets = decoder.feed(data)

            for packet in packets:
                if packet["type"] == "join":
                    username = packet["user"]

                    join_message = protocol.create_server(
                        f"{username} joined the chat."
                    )

                    broadcast(protocol.encode(join_message), client)

                else:
                    broadcast(protocol.encode(packet), client)

        except:
            break

    if username:
        leave_message = protocol.create_server(
            f"{username} left the chat."
        )

        broadcast(protocol.encode(leave_message), client)

    clients.remove(client)
    client.close()

while True:
    client, addr = server.accept()

    print(f"{addr} connected")

    clients.append(client)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()