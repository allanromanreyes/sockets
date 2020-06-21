#Python webserver
import socket

#listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8083))
server_socket.listen()
print("Waiting for connection...")

#pair connection
connection, address = server_socket.accept()
print("Client connected.")

#response function
def send_text(sending_socket, text):
    text = text + "\n"
    data = text.encode()
    sending_socket.send(data)
message = "Welcome, wayfarer"
send_text(connection, message)

#connection_socket.close()
#server_socket.close()