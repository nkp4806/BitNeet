# Changelog

## v0.2 — BNP1 Protocol and Identity

### Added

- Introduced BNP1 (BitNeet Protocol v1)
- Added structured JSON message packets
- Added protocol versioning
- Added `message`, `join`, `leave`, and `server` packet types
- Added JSON encoding and decoding
- Added newline-delimited JSON communication
- Added robust TCP stream buffering and message framing
- Added packet validation
- Added persistent BitNeet user identities
- Added locally generated BitNeet IDs
- Added identity-aware join and leave packets
- Added server-side identity tracking

### Project Structure

- Renamed `client.py` to `bitclient.py`
- Renamed `server.py` to `bitserver.py`
- Added `protocol.py`
- Added `identity.py`
- Added `docs/protocol.md`
- Added `README.md`
- Added `ROADMAP.md`
- Added `.gitignore`

### Chat Features

- Added formatted packet display
- Added join and leave notifications
- Added TCP socket address reuse for easier server restarts
- Added `/help` command
- Added `/quit` command

### Tested

- Verified BNP1 packet encoding and decoding
- Verified packet validation
- Verified client → server BNP1 communication
- Verified server → client BNP1 communication
- Verified TCP message framing
- Verified graceful client disconnect
- Verified server shutdown handling
- Verified persistent local identity generation and loading
- Verified cross-device LAN communication

## v0.1 — Initial LAN Chat

### Added

- Basic TCP client
- Basic TCP server
- Terminal-based chat
- LAN communication