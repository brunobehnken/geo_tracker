import socket
import random
from time import sleep

# Node id
my_id = random.randint(10000, 99999)

# Node initial coordinates
my_x = 0
my_y = 0

# Node pace
my_pace = random.uniform(0.5, 2.5)


def walk():
    """ This method makes the node 'walk' one step. It does so by choosing a random
    number between 1 and 4, which represents one of the following steps:
    +x, -x, +y, -y. Then, it adds or subtracts the node corresponding coordinate
    to effectively move the node."""

    global my_x
    global my_y

    direction = random.randint(1, 4)
    if direction == 1:
        my_x += 1
    elif direction == 2:
        my_x -= 1
    elif direction == 3:
        my_y += 1
    else:
        my_y -= 1


def main():
    # Creates UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 5678)

    print('My pace: ' + str(my_pace))

    # Send my current position to server, then
    # wait 'my_pace' seconds and walk
    while True:
        message = str(my_id) + ',' + str(my_x) + ',' + str(my_y)
        print(message)
        client_socket.sendto(message.encode('utf-8'), server_address)
        sleep(my_pace)
        walk()


main()
