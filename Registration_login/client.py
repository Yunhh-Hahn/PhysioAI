import socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",9999))
# Basically it starts with the server side, and the server side send the prompt username: and it will receive and put into the client message variable
#After that, we input it and client with then send it back to the server and continue

message_username = client.recv(1024).decode()
client.send(input(message_username).encode())

message_password = client.recv(1024).decode()
client.send(input(message_password).encode())

message_usertype = client.recv(1024).decode()
client.send(input(message_usertype).encode())

print(f"Welcome {client.recv(1024).decode()} to PHYSIOAI")
client.close()
