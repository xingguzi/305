#!/usr/bin/env python

#-*- coding:utf-8 -*-


# file:TnlnetClient.py

# author:庄展兴

# datetime:2023/11/21 14:44

# software: PyCharm

'''

this is function description 

'''
# import module your need
import telnetlib
import logging
import time

class TelnetClient():
    def __init__(self):
        self.tn = telnetlib.Telnet()

    #登录设备（设备IP，设备端口号，登录设备账号，登录设备密码）
    def login_host(self,host_ip,port,username,password):
        try:
            self.tn.open(host_ip,port)
        except:
            print('ip为'+host_ip+'端口为'+port+'的设备网络连接失败')
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'login: ', timeout=10)
        self.tn.write(username.encode('utf-8') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password: ', timeout=10)
        self.tn.write(password.encode('utf-8') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('utf-8')
        if 'Login incorrect' not in command_result:
            print('%s登录成功' % host_ip)
            return True
        else:
            print('%s登录失败，用户名或密码错误' % host_ip)
            return False

        # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self,command):
        # 执行命令
        while True:
            command = command
            if command == "exit":
                break
            self.tn.write(command.encode() + b'\n')
            time.sleep(1)
            # 获取命令结果
            command_result = self.tn.read_very_eager().decode('utf-8')
            print('命令执行结果：%s' % command_result)

        # 退出telnet,断开连接
        def logout_host(self):
            self.tn.write(b"exit\n")

if __name__ == '__main__':
    host_ip = '要连接的ip'
    username = '用户名'
    password = '密码'
    port = '00'
    a = 123
    command = '要输入的命令行指令'
    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    if telnet_client.login_host(host_ip,port,username,password):
        telnet_client.execute_some_command(command)
        telnet_client.logout_host()