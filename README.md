# Rpi2PC
Send timestamp/data from Raspberry to PC

In order to send data from Raspberry Pi to a PC a python file (Server.py) on the Raspberry Pi is required and a python file (client.py) on the PC is required.
On the Rpi run sudo python server.py
-> every 3 seconds a message with the timestamp will be displayed

in case you run the server.py twice ... you need to change the port or kill the port in order to reuse it, otherwise the following error shows up: OSError: [Errno 98] Address already in use
-> run the following on the Rpi in order to display the PID in a new line:
  sudo lsof -i :5000
-> now get the PID and run:
  sudo kill -9 <PID>
