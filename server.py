"""EX 2.6 server implementation
   Author:
   Date:
"""
import datetime
import random
import socket
import protocol


def create_server_rsp(cmd):
    if cmd == "TIME":
        print("the time")
        return datetime.datetime + "the time"
    if cmd == "WHORU":
        return "MY NAME IS MENDI SERVER"
    if cmd == "RAND":
        return random.randint(0, 10)
    else:
        return "yes"

    """Based on the command, create a proper response"""
    return "Server response"


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:

        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)
        valid_msg = protocol.check_cmd(cmd)
        if valid_msg:
            print("the time")
            print("recivde message")
            if valid_msg:
                print("the time")
                msg = create_server_rsp(cmd)
                client_socket.send(msg.encode())
            else:
                response = "Wrong command"
        else:
            response = "Wrong protocol"
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage
        # Handle EXIT command, no need to respond to the client
        if cmd == "EXIT":
            break

        # Send response to the client

    print("Closing\n")
    # Close sockets


if __name__ == "__main__":
    main()