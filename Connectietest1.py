import serial
#open serial port at 19k2 (default = 8 data bits, 1 stop bit, no parity)
ser = serial.Serial('COM3', 9600)
print(ser)      # check which port was really used
while True:
    s = ser.read() #read single (raw) byte
    print(s.decode()) #print as hex instead of b'