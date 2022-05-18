import socket

sck = socket.socket()
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
PORT = 50500

sck.bind((host_name, PORT))
sck.listen()

while True:
    print("Listening...")
    connection, address = sck.accept()
    info = socket.gethostbyaddr(address[0])
    print("Connected", info[0], address[0])

    result = connection.recv(1024)
    print(result.decode())

    connection.send(input("Enter your message: ").encode())
