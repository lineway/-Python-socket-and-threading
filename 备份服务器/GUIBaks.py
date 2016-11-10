# -*- encoding:utf-8 -*-
__author__ = 'zhangym'

from tkinter import *
from tkinter.ttk import *
import socket
import struct


def start(host, port):
    pass

class MyFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.grid()
        self.local_ip = '127.0.0.1'
        self.serv_ports = [10888, 20888, 30888]
        self.init_components()

    def init_components(self):
        proj_name = Label(self, text="远程备份服务器")
        proj_name.grid(columnspan=2)

        serv_ip_label = Label(self, text="服务地址")
        serv_ip_label.grid(row=1)

        self.serv_ip = Combobox(self, values=self.get_ipaddr())
        self.serv_ip.set(self.local_ip)
        self.serv_ip.grid(row=1, column=1)

        serv_port_label = Label(self, text="服务端口")
        serv_port_label.grid(row=2)

        self.serv_port = Combobox(self, values=self.serv_ports)
        self.serv_port.set(self.serv_ports[0])
        self.serv_port.grid(row=2, column=1)

        self.start_serv_btn = Button(self, text="启动服务", command=self.start_serv)
        self.start_serv_btn.grid(row=3)

        self.end_serv_btn = Button(self, text="退出服务", command=self.root.destroy)
        self.end_serv_btn.grid(row=3, column=1)

    def get_ipaddr(self):
        host_name = socket.gethostname()
        info = socket.gethostbyname_ex(host_name)
        info = info[2]
        info.append(self.local_ip)
        return info

    def start_serv(self):
        print(self.serv_ip.get(), self.serv_port.get())
        start(self.serv_ip.get(), self.serv_port.get())

if __name__ == '__main__':
    root = Tk()
    root.title("备份服务器")
    root.resizable(False, False)
    app = MyFrame(root)
    app.mainloop()
