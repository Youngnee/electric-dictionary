"""


"""
from socket import socket
import sys
import getpass

HOST = "176.140.7.75"
PORT = 9009
ADDR = (HOST, PORT)

s = socket()
try:
    s.connect(ADDR)
except Exception as e:
    print(e)
    sys.exit()


# 创建网络连接
def main():
    while True:
        print("""
        ============Welcome=============
        -- 1. 注册    2. 登录   3. 退出
        ================================
        """)
        cmd = input("输入选项:")
        if cmd not in ["1", "2", "3"]:
            print("请输入正确选项")
        elif cmd == "1":
            do_rejister()
        elif cmd == "2":
            do_login()
        elif cmd == "3":
            s.send(b"E")
            sys.exit("谢谢使用!")


def do_rejister():
    while True:
        name = input("请输入姓名:\n>>")
        passwd = getpass.getpass()
        passwd1 = getpass.getpass("Again:")

        if (" " in name) or (" " in passwd):
            print("用户名和密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码输入不一致")
            continue

        msg = "R %s %s" % (name, passwd)
        # 发送请求
        s.send(msg.encode())
        # 等待回复
        data = s.recv(128).decode()
        if data == "OK":
            print("注册成功,请记好密码")
            login(name)
        else:
            print(data)
        return


def do_login():
    """
    用户登录
    """
    name = input("用户名:")
    passwd = getpass.getpass("密码:")
    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()  # 接收回复
    if data == "OK":
        print("登录成功")
        login(name)
    else:
        print(data)


# 二级界面
def login(name):
    """
    登录进入后二级操作
    :param name: 用户名
    """
    while True:
        print("""
        ============Welcome=============
        -- 1. 查单词   2. 记录  3. 注销
        ================================
        """)
        cmd = input("输入选项:")
        if cmd not in ["1", "2", "3"]:
            print("请输入正确选项")
        elif cmd == "1":
            do_query(name)
        elif cmd == "2":
            do_hest(name)
        elif cmd == "3":
            return


def do_query(name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        s.send(msg.encode())
        # 回复的可能是单词,也可能查不到
        data = s.recv(2048).decode()
        print(data)


def do_hest(name):
    msg = "H %s" % name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)

    else:
        print(data)


# 测试代码
main()
