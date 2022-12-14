import socket
import subprocess
import threading
import time
import sys

class server(object):
    def __init__(self, ip="127.0.0.1", port=1132):
        self.ip = ip
        self.port = port
        self.ip_port = (ip, port)
        self.socketList = {}

    def shellProcess(self, cmd):
        '''cdm must be a str not byte code'''
        res = subprocess.check_output(cmdCommande, shell=True)



    def synTime(self, *args):
        try:
            myTime = time.strftime("%H:%M:%S", time.localtime())
            soc = args[-1]
            soc.send(myTime.encode(encoding="utf-8"))
            soc.close()
            return 0
        except Exception as e:
            print("some Exception occurred from Function:{funName}! will return this Exception".format(funNam=sys._getframe().f_code.co_name))
            return e

    def getFuncNameObj(self, strFunName):
        if strFunName == "synTime":
            return self.synTime
        if strFunName == "s":
            return self.shellProcess
        return "No func"

    def processSocket(self):
        print("process socket")
        if not self.socketList:
            print("None socketList!!")
        while(self.socketList):
            cmd, soc = self.socketList.popitem()
            print(soc)
            cmdArgs = []
            # cmdFunc = cmd.split(":")[0]
            # 获取客户端调用的函数
            cmdList = cmd["::"]
            cmdFunc = self.getFuncNameObj(cmdList[0])
            # cmdFunc = self.synTime
            cmdContent = cmdList[1]

            cmdArgs.append(soc)
            print("cmdArgs: {}".format(cmdArgs))
            tmpThread = threading.Thread(target=cmdFunc, name=cmdFunc, args=cmdArgs)
            tmpThread.start()
            tmpThread.join()
            print("ended!")
        return True

    def asignSocket(self):
        mainSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        mainSocket.bind(self.ip_port)
        mainSocket.listen(100)
        try:
            while 1:
                clientSocket, clientAddress = mainSocket.accept()
                if clientSocket:
                    print(f"you accept a connection from:{clientAddress}".format(clientSocket=clientSocket))
                    recvMessage = clientSocket.recv(10240).decode(encoding="utf-8")
                    self.socketList.update({recvMessage:clientSocket})
                else:
                    print("failed connection!")
                self.processSocket()
        except:
            mainSocket.close()

serv = server()
serv.asignSocket()