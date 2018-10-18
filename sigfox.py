import serial
import time
import os

def readlineCR(port):
    rv =  ""
    while True:
        ch = port.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv

def detect_sigfox():
    for i in range(0, 6):
        if(os.path.exists('/dev/ttyUSB' + str(i))):
            print("ttyUSB " + str(i) + " exists")
            ser = serial.Serial(port = '/dev/ttyUSB' + str(i), baudrate = 9600, timeout = 0.2)
            ser.write("AT\r\n")
            rcv = readlineCR(ser)
            ser.flushInput()
            ser.close()
            if rcv[:2] == "OK":
                break
        else:
            print("ttyUSB " + str(i) + " not exists")
    return i

out_num = detect_sigfox()
print(out_num)
port = serial.Serial("/dev/ttyUSB" + str(out_num), baudrate=9600, timeout=3.0)  
port.write("AT\r\n")
time.sleep(0.5)
rcv = readlineCR(port)
print(rcv)

while True:
    port.write("AT$I=10\r\n")
    time.sleep(0.5)
    rcv = readlineCR(port)[3:9]
    print(rcv)
    
    port.write("AT$GI?\r\n")
    time.sleep(0.5)
    rcv = readlineCR(port)
    print(rcv)

    print "sent msg"
    port.write("AT$SF=3103C8133039010504800000\r\n")
    time.sleep(5)

    port.write("AT$RC\r\n")
    time.sleep(0.5)
    rcv = readlineCR(port)
    print(rcv)
