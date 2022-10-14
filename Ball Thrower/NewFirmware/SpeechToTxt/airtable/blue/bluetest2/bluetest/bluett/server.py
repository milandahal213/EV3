"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 3.7).
"""

import readline
import code
import bluetooth, time
import ports
hostMACAddress = '' #leave empty
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
print("up and running")
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            #time.sleep(0.1)
            msg = data.decode()
            print(msg)
            shell.push(msg)
            #time.sleep(0.1)
            client.send("Yes") # Echo back to client
except: 
    print("Closing socket")
    client.close()
    s.close()