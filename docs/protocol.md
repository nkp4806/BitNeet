# BitNeet Protocol v1 (BNP1)

## Overview

BNP1 is the communication protocol used by BitNeet.

All communication between the client and the server uses JSON packets.

Each packet is sent as newline-delimited JSON (NDJSON).

---

## Packet Format

Every packet must contain the following fields:

```json
{
    "version": 1,
    "type": "...",
    "user": "...",
    "message": null
}
```

---

## Packet Types

### message

```json
{
    "version": 1,
    "type": "message",
    "user": "Neet",
    "message": "Hello!"
}
```

### join

```json
{
    "version": 1,
    "type": "join",
    "user": "Neet",
    "message": null
}
```

### leave

```json
{
    "version": 1,
    "type": "leave",
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

Packets are newline-delimited JSON (NDJSON).

Each packet ends with a newline (`\n`).

One line equals one complete packet.

---

## Implementation Status

BNP1 v1 is currently implemented for basic message communication.

The current implementation uses newline-delimited JSON, but robust TCP stream buffering and message framing are still under development.