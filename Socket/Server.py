import socket
import os
#   import - kitabxananı idxal edir
#   port və hostlar ilə işləmək üçün kitabxana

sck = socket.socket()
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
PORT = 5040

sck.bind((host_name, PORT))
sck.listen()

while True:
    connection, address = sck.accept()
    print(connection, address)





