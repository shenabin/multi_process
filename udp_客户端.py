import socket

# 创建客户端套接子
udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 准备发送的目的及IP和端口

sendAddr = ("192.168.126.1",7787)

while True:
    senddate = input("请输入要发送的内容：")
    udpsocket.sendto(senddate.encode('utf-8'),sendAddr)

    #准备接受数据
    recv_data = udpsocket.recvfrom(1024)
    print(">>收到数据：%s  from %s" %(recv_data[0].decode('utf-8'),recv_data[1]))
