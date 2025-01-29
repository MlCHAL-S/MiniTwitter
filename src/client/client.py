"""
Module for Client with Logging
"""

import sys
import logging
import grpc
from .. import minitwitter_pb2, minitwitter_pb2_grpc

# Configure logging
logging.basicConfig(
    filename="logs/client.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run(server_ip: str) -> None:
    """
    Run the client application.

    This function establishes a gRPC channel, listens for user input, and processes
    commands to send or retrieve messages or exit the client application.

    Args:
        server_ip (str): The IP address of the server to connect to.
    """
    with grpc.insecure_channel(f"{server_ip}:50051") as channel:
        stub = minitwitter_pb2_grpc.MiniTwitterStub(channel)

        while True:
            command = input(
                "Enter command (SEND <message>, GET <num_of_messages> or EXIT): "
            ).strip()
            logging.info("User entered command: %s", command)

            if command.startswith("SEND "):
                message_text = command[5:]
                response = stub.sendMessage(
                    minitwitter_pb2.MessageRequest(message=message_text)
                )
                print(response.status)
                logging.info("Sent message: '%s' - Response: %s", message_text, response.status)

            elif command.startswith("GET "):
                try:
                    count = int(command[4:])
                    response = stub.getMessages(
                        minitwitter_pb2.MessageListRequest(count=count)
                    )
                    print("Last messages:")
                    for msg in response.messages:
                        print(f"- {msg}")
                    logging.info(
                        "Requested last %d messages - Response: %s",
                        count,
                        response.messages
                    )
                except ValueError:
                    print("Invalid count. Please enter an integer.")
                    logging.warning("User entered invalid count for GET command.")

            elif command == "EXIT":
                print("Exiting...")
                logging.info("Client exited the application.")
                break
            else:
                print("Invalid command. Use SEND <message>, GET <num_of_messages> or EXIT.")
                logging.warning("User entered an invalid command.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m src.client.client <server_ip>")
        sys.exit(1)

    SERVER_IP = sys.argv[1]
    run(SERVER_IP)
