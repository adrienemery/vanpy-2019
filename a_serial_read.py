import serial
from utils import get_port_name

if __name__ == '__main__':
    port = serial.Serial(port=get_port_name(), baudrate=9600)
    while True:
        read_data = port.read_until(b'\r\n')
        print(read_data.strip())
