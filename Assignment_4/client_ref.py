import socket

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc.connect(("localhost", 50007))
    soc.connect(("127.0.0.1", 50007))
    print("Connected.")

    while True:
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