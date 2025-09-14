# OIBSIP_Python_task5
Chat Application 
 What it does:
Allows two people (server and client) to send messages to each other in real-time.
Runs using two Python files:
server.py → waits for a connection.
client.py → connects to the server.
 How it works:
The server listens for someone to connect 
The client connects to the server.
Both keep running in a loop:
Server types → client sees it.
Client types → server sees it.
This works because of socket programming (a way for two programs to talk to each other over a network).
 
