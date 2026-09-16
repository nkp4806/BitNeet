import socket
import threading
import select
import sys
import protocol

SERVER_IP = input("Server IP : ")
PORT = 4806

name = input("Your name : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

disconnected = threading.Event()


def receive():
    decoder = protocol.Decoder()

    while True:
        try:
            data = client.recv(1024)

            if not data:
                disconnected.set()
                break

            packets = decoder.feed(data)

            for packet in packets:
                print(protocol.format_packet(packet))

        except (ConnectionResetError, BrokenPipeError, OSError):
            disconnected.set()
            break


threading.Thread(target=receive, daemon=True).start()

print("\nConnected!\n")

join_packet = protocol.create_join(name)
client.send(protocol.encode(join_packet))


try:
    while not disconnected.is_set():
        ready, _, _ = select.select([sys.stdin], [], [], 0.1)

        if not ready:
            continue

        text = sys.stdin.readline().rstrip("\n")

        if text == "/help":
            print("\nAvailable commands:")
            print("/help  Show available commands")
            print("/quit  Leave BitNeet\n")
            continue

        if text == "/quit":
            leave_packet = protocol.create_leave(name)

            try:
                client.send(protocol.encode(leave_packet))
            except (ConnectionResetError, BrokenPipeError, OSError):
                pass

            client.close()
            print("\nDisconnected.")
            break

        packet = protocol.create_message(name, text)

        try:
            client.send(protocol.encode(packet))
        except (ConnectionResetError, BrokenPipeError, OSError):
            disconnected.set()

    if disconnected.is_set():
        client.close()
        print("\nServer disconnected.")

except KeyboardInterrupt:
    leave_packet = protocol.create_leave(name)

    try:
        client.send(protocol.encode(leave_packet))
    except (ConnectionResetError, BrokenPipeError, OSError):
        pass

    client.close()
    print("\nDisconnected.")