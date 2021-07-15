import socket
from sense_emu import SenseHat

def main():
    sense = SenseHat()
    sense.clear()
    mylist = []
    j = 0
    RGB = []

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("127.0.0.1", 50007))
    print("Connected.")

    while True:
        data = input("Client (q: quit, y: recv data) > ")
        soc.send(data.encode())
        if data == "q":
            soc.close()
            break
        data = (soc.recv(1024)).decode()
        print("cServer > ", data)
        if(data[0] >= "0" or data[0] <= "9"):
            datastr = data.split(",")
            for i in datastr:
                mylist[j] = float(datastr[j])
                j += 1
            j = 0
            THI = 0.81 * mylist[0] + 0.01 * mylist[1] * (0.99 * mylist[0] - 14.3) + 46.3    # 45-110
            if(THI > 60):
                x = 255*(THI-45)/60
                RGB = [x, 0, 255-x]
            elif(THI > 75):
                RGB = [0, 255, 0]
            else:
                x = 255*(THI-75)/110
                RGB = [x, 255-x, 0]
            sense.clear(RGB[0], RGB[1], RGB[2])
        
        # calc THI here
        # display light accd. to THI

    print("Finished.")

if __name__ == "__main__":
    main()

# THI = 0.81 * t + 0.01 * H * (0.99 * t - 14.3) + 46.3
#    - 60   :   blue    0  , 0  , 255
# 60 - 75   :   green   0  , 255, 0
# 75 -      :   red     255, 0  , 0

"""
# Real machine: from sense_hat import SenseHat
# Emulator:     from sense_emu import SenseHat

from sense_emu import SenseHat
sense = SenseHat()
import time

sense.clear()
while True:
    for x in range(0, 255):
        sense.clear(255, x, 0) #red to yellow
    for x in range(0, 255):
        sense.clear(255-x, 255, 0) #yellow to green
    for x in range(0, 255):
        sense.clear(0, 255, x) #green to sky-blue
    for x in range(0, 255):
        sense.clear(0, 255-x, 255) #sky-blue to blue
    for x in range(0, 255):
        sense.clear(x, 0, 255) #blue to purple
    for x in range(0, 255):
        sense.clear(255, 0, 255-x) #purple to red
"""

"""
from sense_emu import SenseHat
import socket
import time

def main():
    sensor_data = [] # 0: temperature, 1: humidity, 2: pressure
    sense = SenseHat()
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc.connect(("localhost", 50007))
    soc.connect(("127.0.0.1", 50007))
    print("Connected.")

    while True:
        for i in range(data)
        t = sense.get_temperature()
        time.sleep(1)
        data = (soc.recv(1024)).decode()
        print("cServer > ", data)
        data = input("cClient > ")
        soc.send(data.encode())
        if data == "q":
            soc.close()
            break
    print("Finished.")

if __name__ == "__main__":
    main()
"""