from flask import Flask
from c_serial_thread import bot

app = Flask(__name__)


@app.route("/distance")
def distance():
    return str(bot.distance)


@app.route("/move/<pos>")
def move(pos):
    bot.move(pos)
    return str(pos)

