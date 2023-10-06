# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Fill in start
host = '10.0.0.38'
server_port = 6789
serverSocket.bind((host, server_port))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    # Fill in start #Fill in end#

    try:

        message = connectionSocket.recv(1024).decode()
        # Fill in start #Fill in end

        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read()
        # Fill in start #Fill in end

        # Send one HTTP header line into socket
        # Fill in start
        header_line = "HTTP/1.0 200 OK\r\n"
        connectionSocket.send(header_line.encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send(message.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        header_line = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(header_line.encode())
        print("404 Not Found")

        # #Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

    serverSocket.close()
