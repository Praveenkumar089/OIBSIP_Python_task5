import socket

client_socket = socket.socket()
client_socket.connect(("localhost", 12345))

while True:
    data = client_socket.recv(1024).decode()
    print("Server:", data)

    message = input("Client: ")
    client_socket.send(message.encode())

client_socket.close()