#!/usr/bin/env python3
"wtf-is-this-robot"
"""
robot speedrun
not able to install pip


CONTROLS:

movement:
w - move forward
s - move backward
d - turn right
a - turn left

steering speed (medium motor):
> - increase steering speed
< - decrease steering speed

speed (large motor):
^ - increase steering speed
v - decrease steering speed
"""

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
import time
import sys
import termios
import tty

def get_key():
    """Reads a single keypress."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)

        if ch1 == '\x1b':  # Arrow keys start with ESC
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            return ch1 + ch2 + ch3
        else:
            return ch1
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


motor_a = LargeMotor(OUTPUT_A) # large
motor_b = LargeMotor(OUTPUT_B) # medium

motor_a.stop_action = 'coast'
motor_b.stop_action = 'coast'

speed_steer = 10
speed = 10
state = 0


print("Press arrow keys or ESC to quit.")
while True:
    key = get_key()

    if key == 'w':
        print("Up")
        motor_a.on(-speed)
        motor_b.off()
        state = 1
    elif key == 's':
        print("Down")
        motor_a.on(speed)
        motor_b.off()
        state = 2
    elif key == 'd':
        print("Right")
        motor_b.on(-speed_steer)
        motor_a.off()
        state = 3
    elif key == 'a':
        print("Left")
        motor_b.on(speed_steer)
        motor_a.off()
        state = 4

    elif key == '\x1b[A':
        speed += 10
        print(speed)
        if state == 1: motor_a.on(-speed)
        elif state == 2: motor_a.on(speed)
    elif key == '\x1b[B':
        speed -= 10
        print(speed)
        if state == 1: motor_a.on(-speed)
        elif state == 2: motor_a.on(speed)


    elif key == '\x1b[C':
        speed_steer += 10
        print(speed_steer)
        if state == 3: motor_b.on(-speed_steer)
        elif state == 4: motor_b.on(speed_steer)
    elif key == '\x1b[D':
        speed_steer -= 10
        print(speed_steer)
        if state == 3: motor_b.on(-speed_steer)
        elif state == 4: motor_b.on(speed_steer)


    elif key == ' ':
        print("stoping")
        motor_a.off()
        motor_b.off()
        state = 0
    else:
        print("Exiting")
        motor_a.off()
        motor_b.off()
        break


    time.sleep(0.05)