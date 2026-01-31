import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("raspberrypi", 5000))

while True:
    print(s.recv(10124).decode("utf-8"))
