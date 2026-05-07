import serial
import time
import subprocess

ser = serial.Serial('/dev/ttyACM0', 9600)

ser.dtr = True
ser.rts = False

time.sleep(1)
subprocess.run(["aplay", "-D", "plughw:2,0", "sstv.wav"])


ser.dtr = False
ser.rts = True

ser.close()
