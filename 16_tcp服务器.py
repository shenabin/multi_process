# 创建套接字
from socket import *
server_socket = socket(AF_INET, SOCK_STREAM)

# 获取本地ip+端口
ser_addr = ("192.168.126.1", 9092)

# bind
server_socket.bind(ser_addr)

server_socket.listen(5)

while True:
    # 如果有新的客户端来链接服务器，那么就产生一个信心的套接字专门为这个客户端服务器
    # newSocket用来为这个客户端服务
    # tcpSerSocket就可以省下来专门等待其他新客户端的链接
    client_socket, client_addr = server_socket.accept()
    while True:
        recv_data = client_socket.recv(1024)
        if len(recv_data) > 0:
            print('胡超1号说',recv_data.decode('utf-8'))
        else:
            print("断开连接")
            client_socket.close()
            break
        send_data = input("胡超说：")
        client_socket.send(send_data.encode('utf-8'))

server_socket.close()
