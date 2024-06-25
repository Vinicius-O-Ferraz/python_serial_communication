import serial
'''
Reading what devices is connected to the computer can be done in the terminal using the python -m serial.tools.list_ports command
'''
ser = serial.Serial(port = 'COM6', baudrate = 9600)

while True:
    value = ser.readline()
    value_in_string =str(value,'UTF-8')
    print(value_in_string)

