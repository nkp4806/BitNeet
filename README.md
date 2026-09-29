# BitNeet

A lightweight, terminal-based messaging application written in Python.

BitNeet is designed to provide simple, direct communication through the terminal without requiring a graphical interface.

## Current Features

- LAN chat
- Client-server architecture
- BNP1 (BitNeet Protocol v1)
- JSON-based communication
- Newline-delimited JSON (NDJSON)
- Robust TCP message framing
- Persistent BitNeet user identities
- Identity-aware join and leave packets
- Server-side identity tracking
- Cross-device communication
- Windows and Android/Termux support

## Requirements

- Python 3.x

## Project Structure

```text
BitNeet/
│
├── bitclient.py
├── bitserver.py
├── protocol.py
├── identity.py
│
├── docs/
│   └── protocol.md
│
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
└── .gitignore
```

## How It Works

BitNeet uses a client-server architecture.

```text
Client
   │
   │ BNP1
   ▼
Server
   │
   │ BNP1
   ▼
Other Clients
```

The server receives messages from connected clients and broadcasts them to the other clients.

## Running BitNeet

### Default Port

BitNeet uses TCP port `4806` by default.

### 1. Start the server

On the machine that will act as the server:

```bash
python bitserver.py
```

You should see:

```text
Server started on port 4806
```

### 2. Start a client

On each client machine:

```bash
python bitclient.py
```

The client will ask for the server IP:

```text
Server IP :
```

Enter the IP address of the machine running `bitserver.py`.

Then enter your username:

```text
Your name :
```

## Protocol

BitNeet uses **BNP1 (BitNeet Protocol v1)** for communication.

BNP1 uses JSON packets transmitted as newline-delimited JSON (NDJSON).

BitNeet also uses persistent user identities.

A BitNeet ID identifies **who** a user is, while the current IP address and port identify **where** the user is connected.

Example join packet:

```json
{
    "version": 1,
    "type": "join",
    "id": "BN-5945073B",
    "user": "Neet",
    "message": null
}
```

For the complete protocol specification, see:

`docs/protocol.md`

## Development Status

BitNeet is currently in early development.

The current implementation supports:

- Basic LAN communication using BNP1
- Robust TCP message framing
- Persistent BitNeet user identities
- Identity-aware join and leave packets
- Server-side identity tracking

## Planned Features

- User-to-user addressing
- Internet communication
- Commands
- Encryption
- File transfer
- Message history
- Improved connection handling

See `ROADMAP.md` for the complete development roadmap.

## License

This project is currently under development.