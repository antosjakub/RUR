#!/bin/bash

# after you run some script which rotates the motor, it will go to hold position - it will make some silent noises and it cannot turn it by hand
# to reset it to default position, run this script

cd /sys/class/tacho-motor/motor1
echo 100 > speed_sp
echo 2000 > time_sp
echo coast > stop_action
echo run-timed > command
