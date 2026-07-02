import socket
import threading

SERVER_IP = input("Server IP : ")
PORT = 9999

name = input("Your name : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))


def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            break


threading.Thread(target=receive, daemon=True).start()

print("\nConnected!\n")

while True:
    text = input()

    if text == "":
        continue

    message = f"{name}: {text}"

    client.send(message.encode())