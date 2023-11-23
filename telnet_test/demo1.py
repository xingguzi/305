import telnetlib
import logging
import time
import sys
import os



#-----------------------------------------------------------------
#  连接telnet服务器
def connettelnet(host,port,username,password,finish):
    try:
        #HOST为telnet要连接设备的IP
        host = host
        #port为telnet要连接设备号的端口号
        port = port
        #建立telnet链接,连接超时时长20s
        tn = telnetlib.Telnet(host,port,timeout=20)
        #设置调试级别,调试等级越高输出信息越多
        tn.set_debuglevel(5)
    except:
        logging.warning()

    #  登陆设备
    tn.read_until("login: ")
    tn.write(str(username) + '\n')
    #输入登陆密码
    tn.read_until("password: ")
    tn.write(str(password) + '\n')

    #判断密码错误提示，如果没有提示说明登陆成功
    if tn.read_until(finish):
        print("*****login incorrect!\n")
    #关闭telnet连接
    tn.close()

    # 进行操作指令
    #------------------------------------------------------------------------------------------------------
    #输入操作指令
    node = input("输入指令")
    #执行操作指令
    tn.write(node.encode('utf-8') + b'\n')
    # 针对单条回显过多，添加等待时间
    time.sleep(2)
    # 获取回条信息
    out = tn.read_very_eager().decode('utf-8')
    # 回显处理，只保留查询到的结果，过滤掉查询输入字符
    out = out.split(node)[-1].strip()
    print(f"{node}   {out}")

    # 进行批量操作指令
    #------------------------------------------------------------------------------------------------------
    #输入操作指令
    nodes = []
    values = []
    for node in nodes:
        tn.write(node.encode('utf-8') + b'\n')
        time.sleep(2)
        value = tn.read_very_eager().decode('utf-8')
        values.add(value)






