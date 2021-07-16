#!/usr/bin/env python3
#client.py

import socket
from sense_emu import SenseHat

def main():
    sense = SenseHat()
    sense.clear()

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
            print("data received: ", datastr)
            mylist = [float(i) for i in datastr]
            THI = 0.81 * mylist[0] + 0.01 * mylist[1] * (0.99 * mylist[0] - 14.3) + 46.3
            if(THI < 60):
                x = 255 * (THI - 45) / 60
                RGB = [x, 0, 255-x]
            elif(THI < 75):
                RGB = [0, 255, 0]
            else:
                x = 255 * (THI - 75 ) / 110
                RGB = [x, 255-x, 0]
            print("THI: "+ str(THI) + ", RGB:" + str(RGB))
            sense.clear(RGB[0], RGB[1], RGB[2])
    print("Finished.")

if __name__ == "__main__":
    main()

# EOF