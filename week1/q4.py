import threading
x = 0
def increment_global():
    global x

    x += 1
def taskofThread(lock1):
    for _ in range(50000):
        lock1.acquire()
        increment_global()
        lock1.release()

def main():
    global x
    x = 0
    lock1 = threading.Lock()
    t1 = threading.Thread(target= taskofThread, args=(lock1,))
    t2 = threading.Thread(target= taskofThread, args=(lock1,))
    t3 = threading.Thread(target= taskofThread, args=(lock1,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
if __name__ == "__main__":
    for i in range(5):
        main()
        print("x = {1} after Iteration {0}".format(i,x))
