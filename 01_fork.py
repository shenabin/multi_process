import os
def fork_test():
    # 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以
    pid = os.fork()

    if pid == 0:
        print("哈哈哈1")

    else:
        print("hello world")

    # 程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），然后复制父进程的所有信息到子进程中
    # 然后父进程和子进程都会从fork()函数中得到一个返回值，在子进程中这个值一定是0，而父进程中是子进程的 id号
    # 在Unix/Linux操作系统中，提供了一个fork()系统函数，它非常特殊。
    # 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）
    # 复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
def fork_pid():
    import os

    # 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以
    rpid = os.fork()

    if rpid == 0:
        print("我是子进程（%s）,我的父进程是（%s）" %(os.getpid(),os.getppid()))

    else:
        print("我是父进程我的pid(%s)，我的子进程有（%s）"%(os.getpid(),rpid))

import os
import time

num = 0

# 注意，fork函数，只在Unix/Linux/Mac上运行，windows不可以
pid = os.fork()

if pid == 0:
    num+=1
    print('哈哈1---num=%d'%num)
else:
    time.sleep(1)
    num+=1
    print('哈哈2---num=%d'%num)

# 打印出来两个进程打印的都是1，多进程就像函数一样，不共享
# 多进程中，每个进程中所有数据（包括全局变量）都各有拥有一份，互不影响