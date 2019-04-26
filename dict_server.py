"""
dict project for aid

"""
from socket import *
import pymysql
import os, sys
import time
import signal

# 全局变量, 从终端输入命令
if len(sys.argv) < 3:
    print("""Run server as:
    python3 dict_server.py 0.0.0.0 9009
    """)
    sys.exit()
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (PORT, PORT)


# DICT_TEXT = "./dict.txt"

# 搭建网络连接
def main():
    # 连接数据库
    db = pymysql.connect("localhost", "root", "123456", "elec_dic")

    # 创建套接字
    s = socket()
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            c, addr = s.accept()
            print("Connect from:", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        pid = os.fork()

        if pid == 0:
            s.close()
            do_request(c, db)  # 处理客户端请求
            sys.exit()
        else:
            c.close()


# 子进程函数,接收请求
def do_request(c, db):
    """
    循环接收请求
    :param c:连接套接字
    :param db:数据库连接对象
    """
    # 接收客户端请求
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), data)
