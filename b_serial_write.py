import serial
import time
from utils import get_port_name


if __name__ == '__main__':
    port = serial.Serial(port=get_port_name(), baudrate=9600)
    while True:
        read_data = port.write(b's10')
        time.sleep(1)
        read_data = port.write(b's90')
        time.sleep(1)