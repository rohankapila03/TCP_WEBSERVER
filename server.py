import socket
# Rohan Kapila (30145862)
# ENSF 462 L2 P2

# get user_two name
user_two_name = input("Enter User 2's Name: ")

# socket creation and bind
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP Socket created")
server_port = 7000
server_socket.bind(('', server_port))
print("socket is binded to the servers address and port number")

# await incoming connections
server_socket.listen(1)

print("server is waiting for a connection to be established")

# accept incoming connection
client_socket, client_address = server_socket.accept()
print("connection established")

# recieve client name and store in variable
user_one_name = client_socket.recv(1024).decode()
print("client name recieved and stored in variable")

# send user_two name to client
client_socket.send(user_two_name.encode())
print("user two name sent to client")

# create chat
while True:
    recieved_msg = client_socket.recv(1024).decode()
    print(f"{user_one_name}: {recieved_msg}")
    print("message recieved")
    if recieved_msg.lower() == "bye":
        break

    msg = input(f"{user_two_name}: ")
    client_socket.send(msg.encode())
    print("message sent")
    if (msg.lower() == "bye"):
        break

client_socket.close()
server_socket.close()
print("socket is closed")
