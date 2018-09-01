# 在 Python 中 使用socket 模块的函数 socket 就可以完成：
# socket.socket(AddressFamily, Type)
# 1.创建TCP套接字
import socket
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("TCP SOCKET CREATE")
# 2.创建UDP套接字
s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("UDP SOCKET CREATE")