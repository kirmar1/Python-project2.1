import serial
import matplotlib.pyplot as plt
from drawnow import *

values = []

plt.ion()

serialArduino = serial.Serial('COM3', 9600)


def plotValues():
    plt.title('Gemeten Lichtsterkte')
    plt.grid(True)
    plt.ylabel('Lichtsterkte in Lux')
    plt.plot(values, 'rx-', label='Lichtsterkte')
    plt.legend(loc='lower right')


# pre-load dummy data
for i in range(0, 10):
    values.append(0)

while True:
    while (serialArduino.inWaiting() == 0):
        pass
    valueRead = serialArduino.readline()

    # check if valid value can be casted
    try:
        valueInInt = int(valueRead)
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                values.append(valueInInt)
                values.pop(0)
                drawnow(plotValues)
            else:
                print(
                "Invalid! negative number")
        else:
            print(
            "Invalid! too large")
    except ValueError:
        print(
        "Invalid! cannot cast")