from threading import Thread
from queue import Queue
import time
# python2 from Queue import Queue


class Processor(Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize()<1000:
                for i in range(100):
                    count += 1
                    str1 = "一代产品：" + str(count)
                    print("生产",str1)
                    q.put(str1)
                    time.sleep(0.1)


class Customer(Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 100:
                for i in range(3):
                   msg = self.name + '消费了' + q.get()
                   print(msg)
            time.sleep(1)


def main():
    global q
    # 初始化初代产品
    for i in range(500):
        if not q.full():
            q.put('初代产品'+str(i))

    # 初始化两个生产者
    for i in range(2):
        processor = Processor()
        processor.start()

    # 初始化两个消费者
    for i in range(5):
        customer = Customer()
        customer.start()

q = Queue()
if __name__ == '__main__':
    main()
