import threading
import serial
from a_serial_read import get_port_name


class Bot:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = serial.Serial(get_port_name(), baudrate=9600)
        self.distance = None
        threading.Thread(target=self.read_worker).start()

    def move(self, pos):
        self.port.write(f's{pos}'.encode())

    def read_worker(self):
        while self.port.is_open:
            read_data = self.port.read_until(b'\r\n')
            try:
                self.distance = int(read_data.strip().decode())
            except ValueError:
                pass


bot = Bot()