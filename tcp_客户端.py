from socket import *

# 1.创建客户端套接子
client_socket = socket(AF_INET, SOCK_STREAM)

# 2.获取服务器ip+端口
ser_addr = ("192.168.126.1",9092)

# 3.连接到服务器

client_socket.connect(ser_addr)

# 4.开启聊天循环

while True:
    send_data = input("胡超1号说:")
    if len(send_data)>0:
        client_socket.send(send_data.encode("utf-8"))

    recv_data = client_socket.recv(1024)
    if len(recv_data)>0:
        print("胡超说：",end=',')
        print(recv_data.decode('utf-8'))

client_socket.close()

