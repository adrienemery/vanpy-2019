require 'sinatra'
require './c_serial_thread'

bot = Bot.new

get '/distance' do
    bot.distance.to_s
end

get '/move/:pos' do |pos|
    bot.move(pos)
end