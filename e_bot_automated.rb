require './c_bot'

bot = Bot.new

loop do
    sleep 0.01
    new_pos = bot.distance.to_i
    new_pos = 10 if new_pos < 10
    new_pos = 90 if new_pos > 90
    bot.move(new_pos)
end
