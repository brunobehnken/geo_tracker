import socket


def main():
    # Creates UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 5678)
    server_socket.bind(server_address)

    while True:
        data = server_socket.recv(2048)  # receive data
        data = data.decode('utf-8')
        print(data)


main()
