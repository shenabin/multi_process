import threading
from threading import Thread
import random
import time
def singe():
    for i in range(3):
        time.sleep(random.random())
        print('i am singing')

def dance():
    for i in range(3):
        time.sleep(random.random())
        print('i am dancing')


def main():
    t1=Thread(target=singe)
    t2=Thread(target=dance)
    # 主线程会等待子线程。所有不用调用join
    t1.start()
    t2.start()

    while True:     # 查看现场数量
        length = len(threading.enumerate())
        print('当前运行的线程数为：%d'%length)
        if length<=1:
            break

        time.sleep(0.5)

if __name__ == '__main__':
    main()