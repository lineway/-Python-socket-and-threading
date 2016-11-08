# -*- encoding:utf-8 -*-
__author__ = 'zhangym'

# py3中的数据传输是二进制字节码，所以需要对数据调用decode()方法

import socket

HOST = ''
PORT = 3214

s = socket.socket()
s.bind((HOST, PORT))

s.listen(5)

# 监听客户端连接，返回的是客户端对象和客户端地址
clnt, addr = s.accept()

print("Client Address:", addr)

while True:
    # buffsize设置为1024
    data = clnt.recv(1024)
    if not data:
        break
    print('Recieve Data:', data.decode('utf-8'))
    # 服务端接收的数据发送回客户端
    clnt.send(data)

clnt.close()
s.close()