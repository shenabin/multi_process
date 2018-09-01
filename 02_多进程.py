from multiprocessing import Process
import os

# 定义函数给父进程调用


def run_poc(name):
    print('子进程运行中（%d）,name = (%s)' % (os.getpid(), name))


def main1():
    # 获取父进程pid
    print("父进程 %d" % os.getpid())
    # 创建子进程对象
    # target=run_poc（要执行的函数）,args = ('test',)（传递的参数，是元组）
    p = Process(target=run_poc, args=('test',))
    # 开启子进程
    print("子进程就要开始执行")
    p.start()
    # 父进程等待子进程结束
    # 等待1s，超时不等候
    # terminate()：不管任务是否完成，立即终止；
    p.join(1)
    print("子进程执行完毕")

# 多参数传递的多进程


def run_para(name, age, **kwargs):
    print("子进程的pid = %d" % os.getpid())
    for i in range(10):
        print("name = %s  age = %d" % (name, age))
        print(kwargs)


def main2():
    print("父进程pid=%d" % os.getpid())
    p = Process(target=run_para, args=('huchao', 18), kwargs={'sex': True})
    p.start()
    p.join()


import time
# 一次创建多个进程


def work1(interval):
    print('子进程%d  父进程%d' % (os.getpid(), os.getppid()))
    time_start = time.time()
    time.sleep(interval)
    time_end = time.time()
    print("work1执行时间为%.2f " % (time_end-time_start))


def work2(interval):
    print('子进程%d  父进程%d' % (os.getpid(), os.getppid()))
    time_start = time.time()
    time.sleep(interval)
    time_end = time.time()
    print("work2执行时间为%.2f " % (time_end-time_start))

# Process的子类


class ProcessClass(Process):
    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    def run(self):
        print('子进程%d  父进程%d' % (os.getpid(), os.getppid()))
        time_start = time.time()
        time.sleep(self.interval)
        time_end = time.time()
        print("work2执行时间为%.2f " % (time_end-time_start))


def main():
    p1 = ProcessClass(1)
    p2 = ProcessClass(2)
    # 调用start函数会自动调用类中的run方法
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
