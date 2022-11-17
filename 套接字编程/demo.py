import socket
import sys
import time

class client(object):

    def __init__(self, item=None):
        self.item = item

    def sendMessage(self, sock, message):
        if sock.send(message):
            return True
        else:
            return False

    def commd(self):
        while True:
            print("start!\n")
            serverAddr = '127.0.0.1'
            # serverAddr = input("please input the server you wanna connect:")
            serverAddr = (serverAddr, 1132)
            print(serverAddr)
            tmpsoc = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            if not tmpsoc.connect(serverAddr):
                print("server connected!")
            else:
                print("connected failed!")
                time.sleep(5)
                continue
            cmd = input("input the command").encode(encoding="unicode-escape")
            self.sendMessage(tmpsoc, cmd)
            print(tmpsoc.recv(10240).decode("utf-8"))


def main():
    cli = client()
    cli.commd()

if __name__ == '__main__':
    main()