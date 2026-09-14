import socket
import threading
import protocol

SERVER_IP = input("Server IP : ")
PORT = 4806

name = input("Your name : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))


def receive():
    decoder = protocol.Decoder()

    while True:
        try:
            data=client.recv(1024)

            if not data:
                break

            packets = decoder.feed(data)

            for packet in packets:
                print(protocol.format_packet(packet))

        except:
            break


threading.Thread(target=receive, daemon=True).start()

print("\nConnected!\n")

join_packet = protocol.create_join(name)
client.send(protocol.encode(join_packet))

while True:
    text = input()

    if text == "":
        continue

    packet = protocol.create_message(name,text)
    client.send(protocol.encode(packet))