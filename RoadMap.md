# BitNeet Roadmap

BitNeet is a lightweight, terminal-based messaging application built from scratch in Python. This roadmap represents the planned evolution of the project.

---

# Current Version

**v0.1**

* ✅ Basic LAN chat
* ✅ Client-server architecture
* ✅ Windows ↔ Android communication
* ✅ Git repository initialized

---

# v0.2 — Foundation

## Goal

Create a proper communication protocol and improve the project's architecture.

### Tasks

* [ ] Design Neet Protocol v1 (NP1)
* [ ] Implement `protocol.py`
* [ ] Replace raw strings with JSON packets
* [ ] Add join packets
* [ ] Add leave packets
* [ ] Add server packets
* [ ] Store usernames on the server
* [ ] Improve disconnect handling

---

# v0.3 — Internet Communication

## Goal

Allow BitNeet to work over the internet.

### Tasks

* [ ] Deploy server to a cloud VPS
* [ ] Connect clients from different networks
* [ ] Handle reconnects
* [ ] Improve connection error messages

---

# v0.4 — Commands

## Goal

Introduce useful terminal commands.

### Tasks

* [ ] /help
* [ ] /exit
* [ ] /clear
* [ ] /online
* [ ] Better command parser

---

# v0.5 — Encryption

## Goal

Secure communication between clients.

### Tasks

* [ ] Research encryption approach
* [ ] Encrypt messages
* [ ] Secure key exchange
* [ ] Verify encrypted communication

---

# v0.6 — File Transfer

## Goal

Allow files to be shared between users.

### Tasks

* [ ] Send files
* [ ] Receive files
* [ ] Transfer progress
* [ ] File validation

---

# v0.7 — Message History

## Goal

Remember previous conversations.

### Tasks

* [ ] Save chat history
* [ ] Load previous messages
* [ ] Search messages

---

# v0.8 — Optimization

## Goal

Improve stability and performance.

### Tasks

* [ ] Refactor networking code
* [ ] Reduce duplicated code
* [ ] Improve reliability
* [ ] Improve error handling

---

# v1.0 — Stable Release

## Goals

* [ ] Stable architecture
* [ ] Stable protocol
* [ ] Internet communication
* [ ] Encryption
* [ ] File transfer
* [ ] Command system
* [ ] Message history
* [ ] Documentation
* [ ] Release on GitHub

---

# Future Ideas

These are ideas, not promises.

* Multiple chat rooms
* Private messaging
* User accounts
* Voice messages
* Plugin system
* Linux package
* End-to-end encrypted groups
* Mobile application
