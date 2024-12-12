
# MiniTwitter

MiniTwitter is a simple gRPC-based microservice application that simulates basic Twitter-like functionality. It allows users to send and retrieve short messages (tweets) via a server-client architecture. This project is designed to demonstrate gRPC communication, Python application structure, and integration with testing and deployment tools.

## Features

- **Send Messages**: Clients can send messages (tweets) to the server.
- **Retrieve Messages**: Clients can fetch the latest messages up to a specified limit.
- **In-Memory Storage**: Messages are stored in memory for simplicity.
- **gRPC Communication**: The project uses Protocol Buffers for defining messages and gRPC for server-client communication.

## Getting Started

Follow these instructions to set up, run, and test MiniTwitter on your local machine.

### Prerequisites

- Python 3.9+
- `pip` (Python package manager)
- Terraform (optional, for deployment)
- gRPC and Protocol Buffers tools

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MlCHAL-S/MiniTwitter.git
   cd MiniTwitter
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the server:**
   ```bash
   python src/server/server.py
   ```

2. **Run the client:**
   ```bash
   python src/client/client.py
   ```

3. **Interact with the client:**
   - `SEND <message>`: Send a message to the server.
   - `GET <num_of_messages>`: Retrieve the last `<num_of_messages>` messages.
   - `EXIT`: Exit the client application.

### Testing

Run the tests using `pytest`:
```bash
pytest
```

The tests include:
- Unit tests for the client and server.
- Smoke tests for the server startup.

### Deployment with Terraform

1. Navigate to the `terraform/` directory:
   ```bash
   cd terraform
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Plan and apply the infrastructure:
   ```bash
   terraform plan
   terraform apply
   ```

This will provision the necessary resources for hosting the MiniTwitter server.

## Configuration

- Modify `proto/minitwitter.proto` to update message or service definitions.
- Adjust server settings in `src/server/server.py` (e.g., port or thread pool size).
- Edit `pylintrc` and `pytest.ini` for linting and testing preferences.

