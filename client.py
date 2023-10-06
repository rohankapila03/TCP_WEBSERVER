# Rohan Kapila (30145862)
# ENSF 462 L2 P2
import socket

# get user_one name
user_one_name = input("Enter User 1's Name: ")

# create and connnect the socket to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket opened")
server_port = 7000
client_socket.connect(('127.0.0.1', server_port))
print("connect to server")

# send message containing user one name to server
client_socket.send(user_one_name.encode())
print("user1 name sent")

user_two_name = client_socket.recv(1024).decode()
print("user two name recieved and stored in variable")

# creating a chat

while True:
    msg = input(f"{user_one_name}: ")
    client_socket.send(msg.encode())
    print("message sent")
    if (msg.lower() == "bye"):
        break

    recieved_msg = client_socket.recv(1024).decode()
    print(f"{user_two_name}: {recieved_msg}")
    print("message recieved")

    if recieved_msg.lower() == "bye":
        break

client_socket.close()
print("socket closed")
