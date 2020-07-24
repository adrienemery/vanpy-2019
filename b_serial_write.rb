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