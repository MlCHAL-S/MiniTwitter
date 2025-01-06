# MiniTwitter

MiniTwitter is a simple gRPC-based microservice application designed to simulate basic Twitter-like functionality. The project implements a server-client architecture where users can send and retrieve short messages (tweets) through defined gRPC methods. This project demonstrates practical usage of gRPC in Python, including the server-side logic, client interactions, and test automation.

---

## Features

- **Send Messages**: Clients can send short text messages (tweets) to the server.
- **Retrieve Messages**: Clients can fetch the latest messages up to a specified limit.
- **In-Memory Storage**: Messages are stored in memory for simplicity.
- **gRPC Communication**: Protocol Buffers are used to define data and service communication.

---

## Architecture

The MiniTwitter project is built with the following components:

- **Server**:
  - Implements gRPC services to handle incoming requests from clients.
  - Stores all messages in a simple in-memory list.
- **Client**:
  - Provides a command-line interface (CLI) for users to send and retrieve messages.
- **Protocol Buffers**:
  - `minitwitter.proto` defines the gRPC methods and message structures.
- **Tests**:
  - Unit tests for client and server functionality ensure the reliability of gRPC methods.

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip` (Python package manager)
- gRPC tools (`grpcio` and `grpcio-tools`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MlCHAL-S/MiniTwitter.git
   cd MiniTwitter
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scriptsctivate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Generate gRPC code (if needed):
   ```bash
   python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/minitwitter.proto
   ```

---

## Running the Application

### Starting the Server
To start the MiniTwitter server, run:
```bash
python server.py
```
The server listens on `localhost:50051` for gRPC connections.

### Running the Client
To start the MiniTwitter client, run:
```bash
python client.py
```
The client provides a simple CLI for interacting with the server:
- `SEND <message>`: Send a tweet to the server.
- `GET <number>`: Retrieve the last `<number>` messages.
- `EXIT`: Exit the client application.

---

## Testing

### Running Tests
The project includes unit tests for both client and server. To run all tests, use:
```bash
pytest
```

### Coverage
The tests validate:
- Correct functionality of gRPC methods (`sendMessage`, `getMessages`).
- Interaction between client and server using mocked gRPC stubs.

---

## Configuration

- Modify `minitwitter.proto` to change gRPC service or message definitions.
- Use `pytest.ini` and `pylintrc` for testing and linting preferences.
