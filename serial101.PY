import serial

ser = serial.Serial('COM8', baudrate = 9600, timeout= 1)

while 1:
    arduinoData = ser.readline().decode()
    print(arduinoData, end = ' ')