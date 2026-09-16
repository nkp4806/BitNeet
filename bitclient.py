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

try:
    while True:
        text = input()

        if text == "/help":
            print("\nAvailable commands:")
            print("/help  Show available commands")
            print("/quit  Leave BitNeet\n")
            continue

        if text == "/quit":
            leave_packet = protocol.create_leave(name)
            client.send(protocol.encode(leave_packet))

            client.close()
            print("\nDisconnected.")
            break

        packet = protocol.create_message(name, text)
        client.send(protocol.encode(packet))

except KeyboardInterrupt:
    leave_packet = protocol.create_leave(name)
    client.send(protocol.encode(leave_packet))

    client.close()
    print("\nDisconnected.")