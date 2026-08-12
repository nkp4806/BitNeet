# Changelog

## v0.2 — BNP1 Protocol

### Added

- Introduced BNP1 (BitNeet Protocol v1)
- Added structured JSON message packets
- Added protocol versioning
- Added `message`, `join`, `leave`, and `server` packet types
- Added JSON encoding and decoding
- Added newline-delimited JSON communication
- Added `protocol.py` as the shared protocol module
- Integrated BNP1 into the client and server

### Project Structure

- Renamed `client.py` to `bitclient.py`
- Renamed `server.py` to `bitserver.py`
- Added `docs/protocol.md`
- Added `README.md`
- Added `ROADMAP.md`
- Added `.gitignore`

### Tested

- Verified BNP1 packet encoding and decoding
- Verified client → server BNP1 communication
- Verified server → client BNP1 communication
- Verified cross-device LAN communication

## v0.1 — Initial LAN Chat

### Added

- Basic TCP client
- Basic TCP server
- Terminal-based chat
- LAN communication