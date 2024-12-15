"""
Module for Client
"""

import sys
import grpc
from .. import minitwitter_pb2, minitwitter_pb2_grpc


def run(server_ip: str) -> None:
    """
    Run the client application.

    This function establishes a gRPC channel, listens for user input, and processes
    commands to send or retrieve messages or exit the client application.

    Args:
        server_ip (str): The IP address of the server to connect to.
    """
    with grpc.insecure_channel(f'{server_ip}:50051') as channel:
        stub = minitwitter_pb2_grpc.MiniTwitterStub(channel)

        while True:
            command = input('Enter command (SEND <message>, GET <num_of_messages> or EXIT): ')

            if command.startswith("SEND "):
                message_text: str = command[5:]
                response: minitwitter_pb2.MessageResponse = stub.sendMessage(
                    minitwitter_pb2.MessageRequest(
                        message=message_text)
                )
                print(response.status)

            elif command.startswith("GET "):
                try:
                    count: int = int(command[4:])
                    response: minitwitter_pb2.MessageListResponse = stub.getMessages(
                        minitwitter_pb2.MessageListRequest(
                            count=count)
                    )
                    print('Last messages:')
                    for msg in response.messages:
                        print(f'- {msg}')
                except ValueError:
                    print('Invalid count. Please enter an integer.')
            elif command == 'EXIT':
                print('Exiting...')
                break
            else:
                print('Invalid command. Use SEND <message>, GET <num_of_messages> or EXIT.')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m src.client.client <server_ip>")
        sys.exit(1)

    server_ip = sys.argv[1]
    run(server_ip)
