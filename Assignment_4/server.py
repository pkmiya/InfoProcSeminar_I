# coding: UTF-8
import datetime
import socket
from sense_emu import SenseHat

def main():
    path = "data.csv"
    
    sense = SenseHat()
    sense.clear()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 50007))
    s.listen(1)
    soc, addr = s.accept()
    print("Connected by " + str(addr))

    while True:
        data = (soc.recv(1024)).decode()
        print("Client > " , data)
        if data == "q":
            # quit
            soc.close()
            break
        elif data == "y":
            # send data (temp, humid, press)
            t = str(sense.get_temperature())
            h = str(sense.get_humidity())
            p = str(sense.get_pressure())
            data = t + "," + h + "," + p
            with open(path, mode="a") as f:
                f.write(datetime.datetime.now() + "," + data + "\n")
        else:
            # normal messaging
            data = input("Server >")
        print("data = " + data)
        soc.send(data.encode())
    print("Finished.")

if __name__ == "__main__":
    main()