# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 09:37:05 2021

@author: Yusuf Morsi
"""
import serial # the PySerial library
import time   # for timing purposes
import enchant as e
dictionary = e.Dict('en_US')

#userInput = "switch"


vowelList = "aeiouAEIOU"
yVowelList = "aeiouyAEIOUY"
consonantList = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
yConsonantList = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
yList = "yY"    
qList = "qQ"
uList = "uU"
puncList = "!.?"


def english_to_pig_latin(userInput):
    lenInput = len(userInput) - 1
    if userInput[lenInput] in puncList: # for punctuation
        puncVar = userInput[lenInput]
        userInput = userInput[:(lenInput)]
    else:
        puncVar = '\0' # this is a null character
        
    if userInput[0] in vowelList: # for vowelList
        userInputVow = userInput + 'yay' + puncVar
        print(userInputVow)
        return userInputVow
        
    elif userInput[0] in yList: # for y
        for i in userInput:
            if i[0] in yList:
                oK = userInput[0].lower()
                userInput = userInput[1:]+oK
            else:
                break;
        nI = userInput[0].upper()
        userInput = nI + userInput[1:]
        userInputY = userInput + 'ey' + puncVar
        print(userInputY)
        return userInputY
        
    elif userInput[0] in qList and userInput[1] in uList: # for Qu
        for i in userInput:
            if userInput[0] in qList and userInput[1] in uList:
                oK = userInput[0].lower()
                ok2 = userInput[1].lower()
                userInput = userInput[2:]+ oK + ok2
            else:
                break;
        nI = userInput[0].upper()
        userInput = nI + userInput[1:]
        userInputQ = userInput + 'ay' + puncVar
        print(userInputQ)
        return userInputQ
        
    else:
        for i in userInput:
            if i[0] in yConsonantList:
                oK = userInput[0].lower()
                userInput = userInput[1:]+oK
            else:
                break;
        nI = userInput[0].upper()
        userInput = nI + userInput[1:]
        userInputCon = userInput + 'ay' + puncVar
        print(userInputCon)
        return userInputCon
            


def pig_latin_to_english(out1):
    lastLetter = len(out1) - 1
    lastLetter2 = len(out1) - 2
    if out1[lastLetter] in puncList:
        newOut = out1[:lastLetter2]   # for removing punctuation 
    else:
        newOut = out1
        
    PLLastLetter = len(newOut) - 1
    PLLastLetter2 = len(newOut) - 2
    
    # if (newOut[PLLastLetter] == 'y'):
    #     theOut = newOut[:PLLastLetter2] # removing the pig latin y
    # else:
    #     print(len(newOut))
    #     return 'Not Pig Latin'
    
    # newLastLetter = (len(theOut) - 1)
    # newLastLetter2 = (len(theOut) - 2)
    # newLastLetter3 = (len(theOut) - 3)
    # newLastLetter4 = (len(theOut) - 4)
    
    # if (theOut[newLastLetter] == 'a') and (theOut[newLastLetter2] == 'y'): # first letter is a vowel
    #     theOut = theOut[:newLastLetter3]
    #     print(theOut)
    #     return theOut
        
    
    lastLetter = (len(out1) - 1)
    lastLetter2 = (len(out1) - 2)
    lastLetter3 = (len(out1) - 3)
    lastLetter4 = (len(out1) - 4)
    
    # below is if it ends in yay   dictionary.check('Howdy')
    
    if ((out1[lastLetter] == 'y') and (out1[lastLetter2] == 'a') and (out1[lastLetter3] == 'y')):
        out1 = out1[:(lastLetter - 1)]
        newLen = len(out1) - 1
        if (dictionary.check(out1) == False):
            out1 = out1[newLen] + out1[:(newLen - 1)]
            print(out1)
        else:
            print(out1)
        
        
    # THE FOLLOWING IS CODE FOR THE PIGLATIN TO ENGLISH FUNCTION
    
    # # below is if it ends in yay! or yay. or yay?
    # elif ((out1[lastLetter] in puncList) and (out1[lastLetter2] = 'y') and (out1[lastLetter3] = 'a') and (out1[lastLetter4] = 'y')):
        
    # # below is if it ends in ay   
    # elif ((out1[lastLetter] = 'y') and (out1[lastLetter2] = 'a')):
        
    # # below is if it ends in ay! or ay? or ay.
    # elif ((out1[lastLetter] in puncList) and (out1[lastLetter2] = 'y') and (out1[lastLetter3] = 'a')):
    
    # # below is if it ends in ey   
    # elif ((out1[lastLetter] = 'y') and (out1[lastLetter2] = 'e')): 
    
    # # below is if it ends in  ey! or ey? or ey.
    # elif ((out1[lastLetter] in puncList) and (out1[lastLetter2] = 'y') and (out1[lastLetter3] = 'e')):


# THE FOLLOWING IS CODE FOR THE OLED

def setup(serial_name, baud_rate):
    ser = serial.Serial(serial_name, baudrate=baud_rate)
    return ser

def close(ser):
    ser.close()
    
def send_message(ser, message):
   if(message[-1] != '\n'):
       message = message + '\n'
   ser.write(message.encode('utf-8'))

def receive_message(ser, num_bytes=50):
    if(ser.in_waiting > 0):
        return ser.readline(num_bytes).decode('utf-8')
    else:
        return None

def main():
    out1 = english_to_pig_latin("hello")
    out2 = pig_latin_to_english(out1) 
    ser = setup("COM4", 115200)
    send_message(ser, out1)
    # send_message(ser, out2)
    time.sleep(3)
    message = receive_message(ser)
    print(message)
    close(ser)

if __name__== "__main__":
   main()



    
 