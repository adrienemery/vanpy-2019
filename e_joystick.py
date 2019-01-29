from pygame import joystick
import pygame
import time

from c_serial_thread import bot

joystick.init()
pygame.display.init()

joy = joystick.Joystick(0)
joy.init()

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
    
    # only update the position if it has changed to prevent spamming the serial port
    if servo_pos != last_servo_pos:
        bot.move(int(servo_pos))
    last_servo_pos = servo_pos

    time.sleep(0.05)

