# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:24:31 2021

@author: Yusuf Morsi
"""
from pyowm import OWM
import datetime

import serial # the PySerial library
import time   # for timing purposes

now = datetime.datetime.now()
owm = OWM('5add5dbd252d8223ab21d41945dd62d4').weather_manager()


def theDay():
    day_string = now.strftime("%m/%d/%Y")
    print(day_string)
    return day_string
    
def theTime():
    time_string = now.strftime("%H:%M:%S")
    print(time_string)
    return time_string

def theWeather(): 
    weather = owm.weather_at_place('San Diego,CA,US').weather
    print(weather)
    return weather.detailed_status

#FOR OLED

def setup(serial_name, baud_rate):
    ser = serial.Serial(serial_name, baudrate=baud_rate)
    return ser

def close(ser):
    ser.close()

def main():
    ser = setup("COM3", 115200)
    close(ser)

"""
Main entrypoint for the application
"""
if __name__== "__main__":
    main()
    
def send_message(ser, message):
   if(message[-1] != '\n'):
       message = message + '\n'
   ser.write(message.encode('utf-8'))

def main():
    ser = setup("COM3", 115200)
    # time.sleep(3)
    send_message(ser, "hello world") # \n
    time.sleep(3)
    close(ser)

   
"""
Receive a message from Serial and limit it to num_bytes (default of 50)
"""
def receive_message(ser, num_bytes=50):
    if(ser.in_waiting > 0):
        return ser.readline(num_bytes).decode('utf-8')
    else:
        return None

def main():
    ser = setup("COM4", 115200) # BLUETOOTH
    while 1 == 1:
        thedate = theDay()
        nowTime = datetime.datetime.now()
        nowTime = str(nowTime)
        thetime = nowTime[11:19]
        # thetime = now.strftime("%H:%M:%S")
        print(thetime)
        theweather = theWeather()
        send_message(ser, thedate + '\n')
        send_message(ser, thetime + '\n')
        send_message(ser, theweather  + '\n')
        time.sleep(.5)
    close(ser)

"""
Main entrypoint for the application
"""
if __name__== "__main__":
   main()


