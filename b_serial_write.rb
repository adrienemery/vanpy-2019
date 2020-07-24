require 'rubyserial'

serialport = Serial.new '/dev/tty.usbmodem141101'

loop do
    p 'Moving to 10'
    serialport.write('s10')
    sleep 2.0
    p 'Moving to 90'
    serialport.write('s90')
    sleep 2.0
end


# if __name__ == '__main__':
#     port = serial.Serial(port=get_port_name(), baudrate=9600)
#     while True:
#         read_data = port.write(b's10')
#         time.sleep(1)
#         read_data = port.write(b's90')
#         time.sleep(1)