import socket

sck = socket.socket()
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
PORT = 50500

sck.connect((host_ip, PORT))

while True:
    sck.send(input("Enter your message: ").encode())
    message = sck.recv(1024)
    print(message.decode())


