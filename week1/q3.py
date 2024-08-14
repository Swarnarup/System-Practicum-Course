import threading
import time

def daemon_th():
    cnt = 0
    while True:
        time.sleep(1)
        # print(time.time())
        print("time = ",cnt)
        cnt+=1

def nondaemon_th(th_delay):
    print("non daemon thread started")
    time.sleep(th_delay)
    print("non daemon thread ended")

if __name__ == '__main__':
    ndt1 = threading.Thread(target=nondaemon_th, args=(6,))
    ndt2 = threading.Thread(target=nondaemon_th, args=(3,))

    dt = threading.Thread(target=daemon_th)
    dt.daemon = True
    ndt1.start()
    ndt2.start()
    dt.start()

