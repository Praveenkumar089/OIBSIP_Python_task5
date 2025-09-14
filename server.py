import socket
server_socket = socket.socket()
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print("Connected with", addr)

while True:
    message = input("Server: ")
    conn.send(message.encode())

    data = conn.recv(1024).decode()
    print("Client:", data)

conn.close()