#PYthon webclient
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8083))
print("Connected!")

#check for messages function
def get_text(receiving_socket):
    buffer = ""
    
    socket_open = True
    while socket_open:
        data = receiving_socket.recv(1024)
        if not data:
            socket_open = False #close socket if no data found
        buffer = buffer + data.decode() #if found, add data to buffer
        
        terminator_pos = buffer.find("\n") #check for terminator
        while terminator_pos > -1:
            message = buffer[:terminator_pos]
            buffer = buffer[terminator_pos + 1:]
            yield message
            terminator_pos = buffer.find("\n") #check again

#message = next(get_text(client_socket)) #iterator for single message retrieval
#print(message)

for message in get_text(client_socket):
    print(message)

#client_socket.close()