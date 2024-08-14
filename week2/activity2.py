
import os

def child(): 
    n = os.fork()
    if n > 0:
        pass
        # print("PID of Parent process is : ", os.getpid())
    else:
        print("PID of Child process is : ", os.getpid())

if __name__ == '__main__':
    print("PID of Parent process is : ", os.getpid())
    child()
    child()
