# -*- encoding:utf-8 -*-
__author__ = 'zhangym'

# py3中的数据传输是二进制字节码，所以需要对数据调用decode()方法
import socket

HOST = '127.0.0.1'
PORT = 3214

s = socket.socket()

try:
    s.connect((HOST, PORT))
    data = "你好！"
    while data:
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024)
        print("Receive from Server:\n", data.decode('utf-8'))
        data = input('Please input an info:\n')
except socket.error as err:
    print(err)
finally:
    s.close()