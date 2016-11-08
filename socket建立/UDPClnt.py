# -*- encoding:utf-8 -*-
__author__ = 'zhangym'

import socket

HOST = '127.0.0.1'
PORT = 3214

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = "你好！"

while data:
    s.sendto(data.encode('utf-8'),(HOST,PORT))
    if data == "bye":
        break
    data,addr = s.recvfrom(1024)
    print('Receive from Server:\n',data.decode('utf-8'))
    data = input('Please input an info:\n')
s.close()