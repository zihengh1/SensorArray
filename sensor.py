import serial
import time
import os
from datetime import datetime
import encode as Enc

def readlineCR(port):
    rv =  ""
    while True:
        ch = port.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv

def detect_sigfox():
    name = "CCLLJJ\r"
    id = -1
    for i in range(0, 6):
        if(os.path.exists('/dev/ttyUSB' + str(i))):
            try:
                ser = serial.Serial(port = '/dev/ttyUSB' + str(i), baudrate = 9600, timeout = 3.0)
                ser.write("AT\r\n")
                state = readlineCR(ser)
                if state[:2] == "OK":
                    id = i
                    ser.write("AT$I=10\r\n")
                    name = readlineCR(ser)
                    ser.close()
                    break
            except Exception as e:
                ser.close()
                print "serial.port is closed"
                print(e)
    return id, name

path = "/home/pi/Data/"
Restful_URL = "https://data.lass-net.org/Upload/SigFox.php"
sigfox_id, device_id = detect_sigfox()
print("sigfox_port: ", sigfox_id)
pivot = device_id.find("\r")
device_id = device_id[(pivot-6) : (pivot)]
print("device_id: ", device_id)

while True:
    data = ""
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(" ")
    for i in range(0, 6):
        if i is not sigfox_id:
            try:
                if(os.path.exists('/dev/ttyUSB' + str(i))):
                    print("dev/ttyUSB " + str(i) + "exists")
                    ser = serial.Serial(
                        port = '/dev/ttyUSB'+str(i),
                        baudrate = 9600,
                        parity = serial.PARITY_NONE,
                        stopbits = serial.STOPBITS_ONE, 
                        bytesize = serial.EIGHTBITS,
                  	)
                    data += '|s%d:%d' % (i, int(ser.read(32)[7].encode('hex'), 16))
                    ser.flushInput()
                    ser.close()
                    time.sleep(0.2)
                else:
                    print("dev/ttyUSB " + str(i) + "not exists")

            except Exception as e:
                ser.close()
                print "serial.port is closed"
                print(e)
    
    data += '|%s_%s' % (str(now_time[0]), str(now_time[1]))
    data_dict = Enc.split_string(data)
    T3_binstr = Enc.dec_to_binstr(data_dict)
    T3_hexstr = Enc.bin_to_hex(T3_binstr)
    print "T3_hexstr : ", T3_hexstr
     
    if sigfox_id is not -1:
        try:
            port = serial.Serial("/dev/ttyUSB" + str(sigfox_id), baudrate=9600, timeout=3.0)
        
            # port.write("AT$I=10\r\n")
            # time.sleep(0.1)
            # device_id = readlineCR(port)
            # print(device_id) 

            port.write("AT$GI?\r\n")
            time.sleep(0.1)
            channel = readlineCR(port)
            print(channel)

            print "sent msg: " + T3_hexstr
            port.write("AT$SF=" + T3_hexstr + "\r\n")
            time.sleep(0.1)

            port.write("AT$RC\r\n")
            time.sleep(0.1)
            port.flushInput()
            port.close()
        
        except Exception as e:
            port.close()
            print "serial.port is closed"
            print(e)
  
    restful_str3 = "wget -O /tmp/last_upload.log \"" + Restful_URL + "?device_id=" + device_id + "&data=" + T3_hexstr + "\""
    # restful_str3 = "wget -O /tmp/last_upload.log \"" + Restful_URL + "?device_id=" + "CCLLJJ" + "&data=" + T3_hexstr + "\""
    os.system(restful_str3)
    data += '|' + device_id
 	
        
    with open(path + str(now_time[0]) + ".txt", "a") as f:
        try: 
            f.write(data + "\n")
        except:
            print "Error: writing to SD"	
    
    time.sleep()
