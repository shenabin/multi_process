from threading import Thread
from threading import Lock
import os
import time

g_num = 0
# 创建一把锁，默认未上锁的
g_mutex = Lock()


def notsafe():
    # 多个线程修改全局变量，就需要互斥锁的参与
    def worker1():
        global g_num
        time_start = time.time()
        for i in range(10000000):
            g_num += 1
        time_end = time.time()
        print('work1执行时间为:%.2f 全局变量=%d' %((time_end-time_start),g_num))

    def worker2():
        global g_num
        time_start = time.time()
        for i in range(10000000):
            g_num += 1
        time_end = time.time()
        print('work2执行时间为::%.2f 全局变量=%d' %((time_end-time_start),g_num))

    def main():
        t1 = Thread(target=worker1)
        t2 = Thread(target=worker2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(g_num)

# 多个线程修改全局变量，就需要互斥锁的参与
def worker1():
    global g_num
    global g_mutex
    time_start = time.time()
    g_mutex.acquire(True) 
    for i in range(1000000):
        # 上锁
        g_num += 1
        # 解锁
    g_mutex.release()
    time_end = time.time()
    print('work1执行时间为:%.2f 全局变量=%d' %((time_end-time_start),g_num))

def worker2():
    global g_num
    global g_mutex
    time_start = time.time()
    g_mutex.acquire(True) 
    for i in range(1000000):
         # 上锁
       
        g_num += 1
        # 解锁
    g_mutex.release()
    time_end = time.time()
    print('work2执行时间为::%.2f 全局变量=%d' %((time_end-time_start),g_num))

def main():  
    t1 = Thread(target=worker1)
    t2 = Thread(target=worker2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(g_num)
    # 48.49 放在基本单位for内部，尼玛，居然执行了49s
    # 7.68 放在for外部，减少了加锁解锁过程，老师的方法不好使

if __name__ == '__main__':
    main()
