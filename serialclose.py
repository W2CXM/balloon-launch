import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

ser.dtr = False
ser.rts = True

ser.close()
