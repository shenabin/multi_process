from multiprocessing import Pool
from multiprocessing import Manager
import time
import random

# 创建进程1用于读取


def write_2_q(q, *args):
    for value in args:
        if not q.full():
            print("写入数据:", value)
            # time.sleep(random.random())
            q.put_nowait(value)
        else:
            print("写入数据完成")
            return

# 创建进程2用于写入


def read_2_q(q):
    while True:
        time.sleep(random.random())
        if not q.empty():
            print("读取数据：", q.get())
        else:
            print("读取完成")
            return


# 主进程用于管理进程1，2
def main():
    po = Pool()
    q = Manager().Queue()  # 使用Manager中的Queue来初始化
    # 这里是阻塞模式，等待write_2_q执行完成在执行(read_2_q
    po.apply(write_2_q, (q, 'n', 'a', 'm', 'e'))
    po.apply(read_2_q, (q,))
    po.close()
    po.join()


if __name__ == '__main__':
    main()
