# 一个结构体用处存放多个函数体对其进行设置，却又互干扰
import threading

# 定义一个全局变量用于存放函数对他的修改
school_student = threading.local()

# 读取
def read_pro():
    print(school_student.name)
    print(threading.current_thread().name)
# 设置
def thread_pro(name):
    # 增加属性
    school_student.name = name
    read_pro()

def main():
    t1 = threading.Thread(target=thread_pro,name='Thead A',args=('huchao',))
    t2 = threading.Thread(target=thread_pro,name='Thead B',args=('xiexue',))
    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__ == '__main__':
    main()