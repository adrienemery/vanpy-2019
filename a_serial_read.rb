require 'rubyserial'

serialport = Serial.new '/dev/tty.usbmodem141101'

buffer = ''

loop do
    next_char = serialport.getbyte&.chr
    buffer += next_char if next_char
    match = buffer.match(/(\d+)\r\n/)
    if match
        data = match[1]
        p data
        buffer = ''
    end
end
