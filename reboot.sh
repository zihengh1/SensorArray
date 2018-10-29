#!/bin/bash

sleep 1
[ -f /home/pi/SensorArray/sensor.py ] && {
    /usr/bin/git -C /home/pi/SensorArray fetch origin
    /usr/bin/git -C /home/pi/SensorArray reset --hard origin/master
    nohup python -u /home/pi/SensorArray/test_program.py &
} || {
    /usr/bin/git clone https://github.com/zihengh1/SensorArray/ /home/pi/SensorArray
    nohup python -u /home/pi/SensorArray/test_program.py &
}

