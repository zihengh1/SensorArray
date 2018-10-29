# SensorArray
use raspberry pi 3B+ to read pm2.5 data from first version MIT sensor <br>

## 1. What do we need? (hardware):
- raspberry pi 3B+
- TP-LINK HUB (7 port)
- Two sockets (one for rpi, one for HUB)
- Five MIT sensors 

## 2. Three different ways to connect to the Internet:
- Wifi
- Ethernet
- Sigfox (optional)

## 3. Where can we set this IOT system:
- Outdoor
- The place where the system can be covered by
- Supported by the stable power

## 4. The files in this repository:
- Sigfox File (the experiment sites have been registered)
- APP (sensor.py is the main program to operate)

## 5. How to check my data?
- Please click this website: https://pm25.lass-net.org/AirBox/detail.php?city=other-ITRI_PM25
- RPI image dowload link: https://drive.google.com/open?id=1C34HaUkcTMwsC1BYE1QCrCPvoj4aS5eY

## 6. Initial this IMG
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install python-serial
- sudo apt-get install git
