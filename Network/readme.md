# Server Client System
# Description
In this project, we build a simple client-server system, where you use
the client to chat with a dummy "math" server. The protocol between the client
and server is as follows.
• The server is first started on a known port.
• The client program is started (server IP and port is provided on the
command line).
• The client connects to the server, and then asks the user for input. The
user enters a simple arithmetic expression string (e.g., "1 + 2", "5 - 6", "3 * 4"). The user's input is sent to the server via the connected socket.
• The server reads the user's input from the client socket, evaluates the
expression, and sends the result back to the client.
• The client should display the server's reply to the user, and prompt the
user for the next input, until the user terminates the client program with
Ctrl+C.
we have two versions of the server:
• Your server program "server1" will be a single process server that can
handle only one client at a time. If a second client tries to chat with the
server while one client's session is already in progress, the second
client's socket operations should see an error.
• Your server program "server2" will be a multi-process server that will
create an execution path for every new client it receives. Multiple clients
should be able to simultaneously chat with the server.

#requirements
you need to install "sudo apt-get update" , and write on the terminal "python3 sever1.py (port_number)" for server 1 or "python3 sever2.py (port_number)" for server 2,
you should run the server before the client , then to run the client , write "python3 client.py (port_number) (ip address)".
