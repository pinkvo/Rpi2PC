import socket
import time
from threading import Timer
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5000))
s.listen(3)         #listen every 3 seconds
print('Server is running.')

def background_controller():
        date_time = datetime.datetime.now()
        format_string = '%Y-%m-%d %H:%M:%S'

        # Convert the datetime object to a string in the specified format
        date_time_string = date_time.strftime(format_string)

        message = 'Hello PC, current timestamp:'
        data = message + date_time_string
        print(data)
        clientsocket.send(bytes(data, "utf-8"))
        Timer(5, background_controller).start()

while True:
        clientsocket, address = s.accept()
        print(f"Connection from (address) has been established.")
        background_controller()
