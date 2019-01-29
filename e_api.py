from flask import Flask
from pyserial import LED

app = Flask(__name__)

led = LED()

@app.route("/on")
def on():
    led.on()
    return "ON"


@app.route("/off")
def off():
    led.off()
    return "OFF"

