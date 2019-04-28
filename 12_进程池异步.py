# 思考，线程闲着的时候该干嘛
# 该睡觉
from multiprocessing import Pool  
import time

def test_main():
    print("执行到这里就闲着了")
    time.sleep(1)
    print("执行带这里就结束了")
    return 'haha'


def test(args):
    print(args)
    print("---------------test------------")


def main():
    po = Pool()
    # func=test_main异步，当callback不占用资源，他需要func返回的资源，只有等到返回的时候会自动调用返回值
    # 就像你妈叫你回家吃饭，做饭的时候主线程在做别的时候，叫的函数发出信号，主线程会通知回调函数回家吃饭
    po.apply_async(func=test_main,callback=test)
    po.close()
    po.join()


if __name__ == '__main__':
    main()
