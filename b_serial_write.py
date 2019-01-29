# Goal: read in data from serial port and print to console
import serial
from serial.tools import list_ports
import time

# get usb port
def get_port_name():
    port_name = ''
    for port_info in list_ports.comports():
        if 'usb' in port_info.device:
            return port_info.device

if __name__ == '__main__':
    port = serial.Serial(port=get_port_name(), baudrate=9600)
    while True:
        read_data = port.write(b's10')
        time.sleep(1)
        read_data = port.write(b's90')
        time.sleep(1)