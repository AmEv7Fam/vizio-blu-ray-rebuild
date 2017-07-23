import serial 
import serial.tools.list_ports 

from win32gui import *	
from win32api import *
from win32con import *

name = "Arduino Uno"

ports = list(serial.tools.list_ports.comports())
for p in ports:
    if(p[1][:len(name)] == name):
        port = p[0]

ser = serial.Serial(port, 9600)

def read_serial():
	while True:
            data = "empty"
            #get the data
            data = ser.readline().decode().strip()
            try:
                func = getattr(Buttons, data)
            except AttributeError:
                    print('function not found "%s"' % (data))
            else:
                func(Buttons)
                    
class Buttons:
    def __init__(self):
        self.last_key=0x0
        
    def FFFFFFFF(self):
        """Repeat code"""
        keybd_event(self.last_key, 0, 0, 0)
        
    def FF956A(self):
        """a"""
        keybd_event(0x41, 0, 0, 0)
    
    def FF9A65(self):
        """Keyboard Up"""
        keybd_event(0x26, 0, 0, 0)
        self.last_key=0x26

    def FF629D(self):
        """Keyboard Down"""
        keybd_event(0x28, 0, 0, 0)
        self.last_key=0x28

read_serial()
