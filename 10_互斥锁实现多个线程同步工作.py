from threading import Thread
from threading import Lock
import time

def task1():
    global mutex1
    global mutex2
    global mutex3
    for i in range(5):
        # 如果第一把锁可以上锁
        if mutex1.acquire():
            print("-------task1-----")
            time.sleep(0.5)
            # 解锁第二把锁，第二个任务就可以执行
            mutex2.release()

def task2():
    global mutex1
    global mutex2
    global mutex3
    for i in range(5):
        if mutex2.acquire():
            print("-------task2-----")
            time.sleep(0.5)
            mutex3.release()

def task3():
    global mutex1
    global mutex2
    global mutex3
    for i in range(5):
        if mutex3.acquire():
            print("-------task3-----")
            time.sleep(0.5)
            mutex1.release()
    
def main():
    # 创建3把锁
    global mutex1
    global mutex2
    global mutex3
    mutex1 = Lock()
    mutex2=Lock()
    # 锁定
    mutex2.acquire()
    mutex3=Lock()
    # 锁定
    mutex3.acquire()
    t1 = Thread(target=task1)
    t2 = Thread(target=task2)
    t3 = Thread(target=task3)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()