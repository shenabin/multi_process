# 创建套接字
from multiprocessing import Process
from socket import *

# 每上线一个客户端就要多建立一个进程，太过于浪费了
def dealwith_data(client_socket, client_addr):
    print('7')
    while True:
        print('9')
        recv_data = client_socket.recv(1024)
        if len(recv_data) > 0:
            print("收到消息 %s 来自 %s" % (recv_data.decode('utf-8'), str(client_addr)))
        else:
            print("客户端%s已经断开连接" % str(client_addr))
            break

        client_socket.send("已收到，谢谢".encode('utf-8'))




def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 这是端口可以一直占用，不会出现掉线了不能再用
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 获取本地ip+端口
    ser_addr = ("192.168.126.1", 9093)
    # 绑定IP端口
    server_socket.bind(ser_addr)


    # 监听，把主动套接字变为被动套接字
    server_socket.listen(15)
    try:
        while True:
            print("等待连接")
            # 接受客户端连接，有 连接的时候就新建一个客户端套接字处理
            client_socket, client_addr = server_socket.accept()
            print("连接成功 %s" %str(client_addr))
            try:
                p = Process(target=dealwith_data, args=(client_socket, client_addr))
                p.start()

            finally:
                # 因为套接字已经转为参数传递给函数处理，有了备份，就可以删除了
                client_socket.close()
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()