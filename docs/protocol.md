# BitNeet Protocol v1 (BNP1)

## Overview

BNP1 is the communication protocol used by BitNeet.

All communication between the client and the server uses JSON packets.

Each packet is sent as newline-delimited JSON (NDJSON).

---

## Packet Format

Packets contain the following common fields:

```json
{
    "version": 1,
    "type": "...",
    "user": "...",
    "message": null
}
```

---

## Identity

Each BitNeet installation has a persistent BitNeet ID.

The BitNeet ID identifies the user, while the IP address and TCP port identify where the user is currently connected.

BitNeet IDs are currently generated locally and stored in:

`~/.bitneet/identity.json`

The current identity system does not provide authentication or cryptographic proof of identity.

---

## Packet Types

### message

```json
{
    "version": 1,
    "type": "join",
    "user": "Neet",
    "message": null
}
```

### join

```json
{
    "version": 1,
    "type": "join",
    "id": "BN-5945073B",
    "user": "Neet",
    "message": null
}
```

### leave

```json
{
    "version": 1,
    "type": "leave",
    "id": "BN-5945073B",
    "user": "Neet",
    "message": null
}
```

### server

```json
{
    "version": 1,
    "type": "server",
    "user": "SERVER",
    "message": "Neet joined the chat."
}
```

---

## Transport

Packets are transmitted over TCP using newline-delimited JSON (NDJSON).

Each packet ends with a newline (`\n`).

TCP is a stream protocol, so a single `recv()` call does not necessarily contain exactly one packet.

BitNeet uses a decoder buffer to collect incoming data and split it into complete packets whenever a newline is received.

This allows BitNeet to correctly handle packets that are:

- Split across multiple TCP reads
- Multiple packets received in a single TCP read

---

## Implementation Status

BNP1 v1 is currently implemented.

The current implementation supports:

- JSON message packets
- Join and leave packets with persistent BitNeet IDs
- Server packets
- Newline-delimited JSON (NDJSON)
- TCP stream buffering and message framing
- Packet validation
- Persistent local identity storage