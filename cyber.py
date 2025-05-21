# *****************************************
# *                                       *
# *               V A M S I              *
# *                                       *
# *****************************************
#Listening
import socket
ip = input("enter a ip address:")
port = int(input("enter a port address:"))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()
print("waiting for keystrokes......")
client_socket, client_addr = server.accept()
while True:
    data = client_socket.recv(4024).decode()
    print(data)
