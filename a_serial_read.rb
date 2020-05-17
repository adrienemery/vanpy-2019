require 'rubyserial'

serialport = Serial.new '/dev/ttyACM0'

buffer = []


loop do
    buffer += serialport.getbyte
    data = buffer.pack('c*')
    if data.match(/\\r\\n/)
        p data
        buffer = []
end
