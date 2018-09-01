# 作为服务器用
from socket import *
# 创建套接字
udpsocket = socket(AF_INET,SOCK_DGRAM)
# 绑定本机ip
addr = ('',7787)
udpsocket.bind(addr)

while True:
    recvdata = udpsocket.recvfrom(1024)
    print('<<收到数据：%s from %s' %(recvdata[0].decode('utf-8'),recvdata[1]))
    if len(recvdata)<=0:
        udpsocket.close()
        break
# 收到数据：中华名组画岁 from ('192.168.126.129', 47483)
    send_data = input("\r\n>>请输入要发送的：")
    udpsocket.sendto(send_data.encode('utf-8'),recvdata[1])
