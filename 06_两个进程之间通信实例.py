from multiprocessing import Queue 
from multiprocessing import Process
import time
import random

def write_2_q(q):
    for value in ['A','B','C','D']:
        if not q.full():
            print("写入数据:",value)
            # time.sleep(random.random())
            q.put_nowait(value)
        else:
            print("写入数据完成")
            return

def read_2_q(q):
    while True:
        time.sleep(random.random())
        if not q.empty():
            print("读取数据：", q.get())
        else:
            print("读取完成")
            return


def main():
    # 新建一个队列可以存放三条数据
    q = Queue(3)

    pw = Process(target=write_2_q,args =(q,))
    pr = Process(target=read_2_q,args =(q,))
    pw.start()
    pr.start()
    pw.join() 
    pr.join()


if __name__ == '__main__':
    main()