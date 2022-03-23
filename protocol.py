"""EX 2.6 protocol implementation
   Author:
   Date:
"""

LENGTH_FIELD_SIZE = 2
PORT = 8820


def check_cmd(data):
    if data == "TIME" or data == "WHORU" or data == "RAND" or data == "EXIT" or len(data) < 100 or data == False:
        return True
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    return False


def create_msg(data):
    slengh = data
    length = str(len(data))
    zfill_length = length.zfill(2)
    data = zfill_length + slengh
    print(data)
    """Create a valid protocol message, with length field"""
    return data


def get_msg(my_socket):
    valid_msg = my_socket.recv(2).decode()
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    my_socket.recv(int(valid_msg)).decode()
    if not valid_msg.isdigit():
        return False
    print(my_socket.recv(int(valid_msg)).decode())
    return my_socket.recv(int(valid_msg)).decode()


def get_int(my_socket):
    valid_msg = my_socket.recv(2).decode()
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    print(my_socket.recv(int(valid_msg)).decode())
    if not valid_msg.isdigit():
        return "False"
    print(my_socket.recv(int(valid_msg)).decode())
    return int(valid_msg)