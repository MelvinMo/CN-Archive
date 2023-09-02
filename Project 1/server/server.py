import os
import pickle
from socket import *
import sys
import random

rname = "127.0.0.1"
port = 2121
serversocket = socket(AF_INET,SOCK_STREAM)
serversocket.bind((name,port))
print("ready:")
print("listening...")
serversocket.listen(5)

while True:
    connectionsocket , addr = serversocket.accept()
    command_msg  = connectionsocket.recv(2048).decode()
    if command_msg == "help" or command_msg == "start" :
        connectionsocket.send("\nhelp\t = show this help\nlist\t = list files\npwd\t = show current directory\ncd dir_name\t = change directory\ndwld file_path\t = download file\n exit\t = quit".encode())
    elif command_msg == "exit":
        break
    elif command_msg[0] == 'c' and command_msg[1] == 'd':
        print("recieved instruction : cd ")
        cmnd2 = command_msg.split(" ")
        os.chdir(cmnd2[1])
    elif command_msg == "pwd" :
        print("recieved instruction : pwd")
        connectionsocket.send(os.getcwd().encode())
    elif command_msg == "list":
        print("recieved instruction : list")
        TotalSize=0
        AllFiles=os.scandir(os.getcwd())
        DF=""
        for i in AllFiles:
            q=i.name
            z=os.stat(i.name).st_size
            if i.is_dir():
                DF=f">		{q} - {z}\n"
            if i.is_file():
                DF=f"		{q} - {z}\n"
            TotalSize+=z
            connectionsocket.send(bytes(DF,'utf-8'))
        
    elif command_msg[0]=='d' and command_msg[1]=='w' and command_msg[2]=='l' and command_msg[3]=='d':
        print("recieved instruction : dwld")
        cmnd1 = command_msg.split(" ")
        dwld_filename = cmnd1[1]
        dwnlport = random.randrange(3000, 50000)
        dwnlsocket = socket(AF_INET, SOCK_STREAM)
        dwnlsocket.bind(("127.0.0.1", dwnlport))
        connectionsocket.send(str(dwnlport).encode())
        dwnlsocket.listen(5)
        while(True):
            dwldconnectionsocket, addrdwld = dwnlsocket.accept()
            confirm_msg = dwldconnectionsocket.recv(2048).decode()
            file = open(dwld_filename, "rb")
            dwldpacket = file.read()
            file.close()
            dwldconnectionsocket.send(dwldpacket)
            confirm_msg2 = dwldconnectionsocket.recv(2048)
            dwldconnectionsocket.close()
            dwnlsocket.close()
            break
            print("finish")
    connectionsocket.close()