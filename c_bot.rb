require 'rubyserial'

class Bot
    attr_reader :read_worker, :pos, :distance, :serialport, :stopped

    def initialize
        @distance = 0
        @pos = 0
        @stopped = false
        @serialport = Serial.new '/dev/tty.usbmodem141101'
        Thread.new { read_worker }
    end

    def stop
        @stopped = true
    end

    def move(pos)
        @pos = pos
        @serialport.write("s#{pos}")
        p "moving to #{pos}"
    end

    def read_worker
        buffer = ''

        while !@stopped
            # TODO read the serial port
            next_char = @serialport.getbyte&.chr
            buffer += next_char if next_char
            match = buffer.match(/(\d+)\r\n/)
            if match
                @distance = match[1]
                buffer = ''
            end
        end
        puts 'Exiting read thread!'
    end
end


# bot = Bot.new