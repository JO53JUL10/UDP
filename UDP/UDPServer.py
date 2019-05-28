#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_DGRAM, AF_INET
from random import randint
from time import time

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Waiting for connections")
while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
    # Randomly drop packet
    randomNumber = randint(0,9)
    if randomNumber >= 4:
	    continue
    # Campture time when packet was received
    startTime = time()
    # Capitalize the message from the client
    print(message, address)
    message = message.upper()
    serverSocket.sendto(message, address)
    # Capture time when the packet was delivered to client
    endTime = time()
    totalTime = (endTime - startTime)
    print("Total time for response is: " + str(totalTime) + " ms")
serverSocket.close()

#Configure the server so that it randomly drops packets.
#Include information about how long each response took. This will be the RTT.