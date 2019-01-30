from serial.tools import list_ports

def get_port_name():
    port_name = ''
    for port_info in list_ports.comports():
        if 'usb' in port_info.device:
            return port_info.device