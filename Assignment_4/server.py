# coding: UTF-8
import socket

def main():
    send_data = "Send your data"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 50007))
    s.listen(1)
    soc, addr = s.accept()
    print("Connected by " + str(addr))

    while True:
        # data = input("Server > ")
        data = send_data 
        print("data = " + data)
        soc.send(data.encode())
        data = (soc.recv(1024)).decode()
        print("Client > " , data)
        if data == "q":
            soc.close()
            break
    print("Finished.")

if __name__ == "__main__":
    main()