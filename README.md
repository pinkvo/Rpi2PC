# Rpi2PC
Send timestamp/data from Raspberry to PC

Both, Raspberryp PI and PC have to be in the same wifi.

In order to send data from Raspberry Pi to a PC a python file (server_rpi.py) on the Raspberry Pi is required and a python file (client_PC.py) on the PC is required.
On the Rpi run sudo python server_rpi.py
-> every 3 seconds a message with the timestamp will be displayed

in case you run the server.py twice ... you need to change the port or kill the port in order to reuse it, otherwise the following error shows up: OSError: [Errno 98] Address already in use
-> run the following on the Rpi in order to display the PID in a new line:
  sudo lsof -i :5000
-> now get the PID and run:
  sudo kill -9 PID
