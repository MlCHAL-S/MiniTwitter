# MiniTwitter

MiniTwitter is a simple gRPC-based microservice application designed to simulate basic Twitter-like functionality. The project implements a server-client architecture where users can send and retrieve short messages (tweets) through defined gRPC methods. This project demonstrates practical usage of gRPC in Python, including the server-side logic, client interactions, and test automation.

---

## Features

- **Send Messages**: Clients can send short text messages (tweets) to the server.
- **Retrieve Messages**: Clients can fetch the latest messages up to a specified limit.
- **In-Memory Storage**: Messages are stored in memory for simplicity.
- **gRPC Communication**: Protocol Buffers are used to define data and service communication.
- **CI/CD**: Automated testing and linting through GitHub Actions.
- **Logging System**: A `logs/` folder is used for debugging and tracking system behavior.
- **High Test Coverage**: Over **90%** code coverage with `pytest`.
- **Linting**: `pylint` reports **10/10** for both `client.py` and `server.py`.

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

### Set PYTHONPATH
```bash
export PYTHONPATH=src:$PYTHONPATH
```

### Starting the Server
To start the MiniTwitter server, run:
```bash
python -m src.server.server
```
The server listens on `localhost:50051` for gRPC connections.

### Running the Client
To start the MiniTwitter client, run:
```bash
python -m src.client.client
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

Tests cover over 90% of the code:
```bash
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
src/client/client.py      39      5    87%   73-78
src/server/server.py      26      1    96%   77
----------------------------------------------------
TOTAL                     65      6    91%
```

### Linting
The project follows PEP8 coding standards. `pylint` results:
```bash
client.py: 10/10
server.py: 10/10
```

## Deployment

### Infrastructure as Code (Terraform) 
Infrastructure is managed with Terraform: 
* **`main.tf`**: Defines AWS resources (VPC, EC2, Security Groups).
* **`vars.tf`**: Configurable parameters.
* **`output.tf`**: Stores deployment details.

**Initialize Terraform**:
```bash
terraform init
```

### Using Ansible

To deploy the MiniTwitter server using Ansible:

```bash
ansible-playbook -i ansible/inventory.ini ansible/config.yaml
```

### Running the Client
Once the server is deployed and running, you can start the client by running:
```bash
python -m src.client.client <server_ip>
```
Replace `<server_ip>` with the actual IP address of your deployed server.

### Continuous Integration (CI)
CI is handled with GitHub Actions (`.github/workflows/ci.yaml`): 
* Runs on pull requests to `main`.
* Steps include:
  * **Code checkout**
  * **Python environment setup**
  * **Dependency installation**
  * **Linting with `pylint`**
  * **Running tests with `pytest`**

---

## Contributors 
* **`MlCHAL-S`** 
* **`olivblvck`** 
* **`KubaSienski`** 

---

## Documentation
For a detailed explanation, refer to [the full documentation](docs/documentation.pdf).
