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