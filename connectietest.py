import serial
import time

#The following line is for serial over GPIO
port = 'COM3'


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

i = 0

while (i < 4):
    # Serial write section

    setTempCar1 = 63
    setTempCar2 = 37
    ard.flush()
    setTemp1 = str(setTempCar1)
    setTemp2 = str(setTempCar2)
    print("Python value sent: ")
    print(setTemp1)
    ard.write(setTemp1.encode())
    time.sleep(1) # I shortened this to match the new value in your Arduino code

    # Serial read section
    msg = ard.read(ard.inWaiting()) # read all characters in buffer
    print("Message from arduino: ")
    print(msg.decode())
    i = i + 1
else:
    print("Exiting")
exit()