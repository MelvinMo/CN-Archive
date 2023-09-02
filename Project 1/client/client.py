import os
import pickle
from socket import *
import time
import sys

start = 0
while True:
    name = "127.0.0.1"
    port = 2121
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((name, port))
    if start == 0:
        command = "start"
    else:
        command = input("waiting for your command : ")
    if command == "exit":
        clientsocket.send(command.encode())
        break
    clientsocket.send(command.encode())
    if command == "list":
         time.sleep(.25)
         b=clientsocket.recv(4096)
         if not b:
             break
         print(b.decode('utf-8'))          
    elif command[0]=='d' and command[1]=='w'and command[2]=='l'and command[3]=='d':
        cmnd22= command.split(" ")
        dwnlfilename = cmnd22[1]
        port_recive = int(clientsocket.recv(2048).decode())
        dwld_server = "127.0.0.1"
        dwld_socket = socket(AF_INET, SOCK_STREAM)
        dwld_socket.connect((dwld_server,  port_recive))
        dwld_socket.send("connected".encode())
        dwld_data = dwld_socket.recv(2097152)
        file = open(dwnlfilename, 'wb')
        file.write(dwld_data)
        file.close()
        dwld_socket.send("success".encode())
    else:
        sentence = clientsocket.recv(2048)
        print(sentence.decode())
        sentence = ''
    start = start+1