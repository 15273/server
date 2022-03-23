import socket
import protocol


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", protocol.PORT))

    while True:
        print("the order option is \n1.TIME\n2.WHORU\n"
              "3.RAND\n4.EXIT")
        user_input = input("Enter command\n")
        # Check if user entered a valid command as defined in protocol
        valid_cmd = protocol.check_cmd(user_input)

        if valid_cmd:
            print("kxed")
            user_input = protocol.create_msg(user_input)
            my_socket.send(user_input.encode())
            if user_input[2:] == "EXIT":
                break
            length = my_socket.recv(2).decode()
            print(length)
            data = my_socket.recv(int(length)).decode()
            print(data)

            if data != "False":
                print(data)

            else:
                print("Response not valid\n")
        else:
            print("Not a valid command")

    print("Closing\n")
    # Close socket


if __name__ == "__main__":
    main()
