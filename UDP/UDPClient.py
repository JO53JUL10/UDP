#UDPClient.py

from socket import socket, timeout, SOCK_DGRAM, AF_INET

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = raw_input('Input lowercase sentence: ')
clientSocket.sendto(message, (serverName, serverPort))
try:
    modifiedMessage, addr = clientSocket.recvfrom(2048)
    print(modifiedMessage, addr)
except timeout:
    print("Socket timed out. Not answer received in the last second.")
clientSocket.close()

#Allow the client to give up if no response has been reveived within 1 second.