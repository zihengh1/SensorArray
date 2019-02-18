#!/bin/bash

sleep 10

#kill python run more then 1 day
sudo killall -o 23h59m python

[ -f /home/pi/SensorArray/sensor.py ] && {
    /usr/bin/sudo git -C /home/pi/SensorArray fetch --all
    /usr/bin/sudo git -C /home/pi/SensorArray reset --hard origin/master
    /usr/bin/sudo nohup python -u /home/pi/SensorArray/sensor.py &
} || {
    /usr/bin/git clone https://github.com/zihengh1/SensorArray/ /home/pi/SensorArray
    /usr/bin/sudo nohup python -u /home/pi/SensorArray/sensor.py &
}

