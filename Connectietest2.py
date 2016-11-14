import serial
import time

#The following line is for serial over GPIO
port = 'COM3'


ard = serial.Serial(port,9600)
time.sleep(2) # wait for Arduino

i = 0


# Serial write section

test1 = "B1000"
ard.flush()
ard.write(test1.encode())

while True:
    time.sleep(1)
    # Serial read section
    msg = ard.read(ard.inWaiting()) # read all characters in buffer
    print("Message from arduino: ")
    print(msg.decode())
    i = i + 1

else:
    print("Exiting")
exit()