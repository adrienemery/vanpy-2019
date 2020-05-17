# require 'serialport'


class Bot
    attr_reader :read_worker, :pos, :distance

    def initialize
        @distance = 0
        @pos = 0
        @stopped = false
        Thread.new { read_worker }
    end

    def stop
        @stopped = true
    end

    def move(pos)
        @pos = pos
        p "moving to #{pos}"
    end

    def read_worker
        while !@stopped
            # TODO read the serial port
            @distance += 1
            sleep 1
        end
        puts 'Exiting read thread!'
    end
end


# bot = Bot.new