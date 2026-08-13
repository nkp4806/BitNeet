import socket
import threading
import protocol

SERVER_IP = input("Server IP : ")
PORT = 4806

name = input("Your name : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))


def receive():
    while True:
        try:
            data = client.recv(1024)

            if not data :
                break
            packet = protocol.decode(data)

        except:
            break


threading.Thread(target=receive, daemon=True).start()

print("\nConnected!\n")

while True:
    text = input()

    if text == "":
        continue

    packet = protocol.create_message(name,text)
    client.send(protocol.encode(packet))