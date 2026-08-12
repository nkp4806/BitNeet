import socket
import threading
import protocol

HOST = "0.0.0.0"
PORT = 9999

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    while True:
        try:
            data = client.recv(1024)

            if not data:
                break

            packet = protocol.decode(data)

            broadcast(protocol.encode(packet), client)

        except:
            break

    clients.remove(client)
    client.close()

while True:
    client, addr = server.accept()

    print(f"{addr} connected")

    clients.append(client)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()