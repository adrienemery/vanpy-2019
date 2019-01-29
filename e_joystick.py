from pygame import joystick
import pygame
import time

from pyserial import servo, led

joystick.init()
pygame.display.init()

joy = joystick.Joystick(0)
joy.init()

led_state = False
last_led_state = False

servo_pos = 0
last_servo_pos = 0

while True:
    # refresh pygame joystick inputs
    pygame.event.get()
    pygame.event.pump()
    
    # update servo position
    servo_pos = joy.get_axis(0)
    # joystick input is between -1 and 1 so we
    # remap it to 0 to 180
    servo_pos *= 90
    servo_pos += 90
    if servo_pos != last_servo_pos:
        servo.move(int(servo_pos))
    last_servo_pos = servo_pos

    # update led state
    led_state = joy.get_button(13)
    if led_state != last_led_state:
        if led_state :
            led.on()
        else:
            led.off()
    last_led_state = led_state

    time.sleep(0.05)

