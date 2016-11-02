import serial
import matplotlib.pyplot as plt
from drawnow import *

values = []

plt.ion()
cnt = 0

serialArduino = serial.Serial('COM3', 9600)


def plotValues():
    plt.title('Gemeten buitentemperatuur')
    plt.grid(True)
    plt.ylabel('Graden Celsius')
    plt.xlabel('Tijd in seconden')
    plt.plot(values, 'rx-', label='°C')
    plt.legend(loc='upper left')


# pre-load dummy data
for i in range(0, 11):
    values.append(0)

while True:
    while (serialArduino.inWaiting() == 0):
        pass
    valueRead = serialArduino.readline()

    # check if valid value can be casted
    try:
        valueInInt = int(valueRead)
        print(valueInInt)
        if valueInInt <= 35:
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