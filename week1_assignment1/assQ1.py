import threading
import random
import time
import sys

# print = lambda x : sys.stdout.write("%s \n"%x)

class diningPhil(threading.Thread):

    running = True
    
    def __init__(self, xname, fork_l, fork_r):
        threading.Thread.__init__(self)
        self.name = xname
        self.fork_l = fork_l
        self.fork_r = fork_r
        self.generous = False
        self.cnt = 0

    def run(self):
        while(self.running):
            time.sleep(random.uniform(1,1.3))
            # time.sleep(4)
            # print(str(self.name)+" is hungry.")
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork_l, self.fork_r


        if self.generous:
            while self.running:
                fork1.acquire(blocking=True)
                # locked = fork2.acquire(False)
                if fork2.acquire(blocking = False):
                    self.dining()
                    fork1.release()  
                    fork2.release()
                    continue                  
                fork1.release()
                # print(self.name ," swaps forks")
                # fork1, fork2 = fork2, fork1
            else:
                # print(str(self.name)+"EEEEXXXXXXXXX")
                return

                
        else:
            while self.running:
                fork1.acquire(blocking=True)
                # locked = fork2.acquire(False)
                # if fork2.acquire(blocking = False):
                #     self.dining()
                #     fork1.release()  
                #     fork2.release()
                #     continue                  
                # fork1.release()
                fork2.acquire(blocking=True)
                self.dining()
                fork1.release()
                fork2.release()
                
            else:
                # print(str(self.name)+"EEEEXXXXXXXXX")
                return
    
    def dining(self):
        # print(str(self.name)+" starts eating")
        self.cnt+=1
        time.sleep(random.uniform(1,1.8))
        # time.sleep(4)
        # print(str(self.name)+" finishes eating")

def dining_philosopgers(running_time):
    forks = [threading.Lock() for n in range(5)]
    name_phil_l = ["1", "2", "3", "4", "5"]
    phils = [diningPhil(name_phil_l[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
    random.seed()
    diningPhil.running=True
    phils[0].generous = True
    phils[2].generous = True
    for p in phils:
        p.start()
    time.sleep(running_time)
    diningPhil.running = False
    # print("finished.")
    for p in phils:
        p.join()
    list_count = []
    for p in phils:
        list_count.append(p.cnt)
    return list_count

# l1 = dining_philosopgers(100)

# print(l1)

#########################

rt = 10
ll=[]
for i in range(10):
    l1 = dining_philosopgers(rt)
    ll.append(l1)
    rt+=10

import matplotlib.pyplot as plt

plt.plot([i for i in range(10)], [ll[i][0] for i in range(10)], label = "p1")
plt.plot([i for i in range(10)], [ll[i][1] for i in range(10)], label = "p2")
plt.plot([i for i in range(10)], [ll[i][2] for i in range(10)], label = "p3")
plt.plot([i for i in range(10)], [ll[i][3] for i in range(10)], label = "p4")
plt.plot([i for i in range(10)], [ll[i][4] for i in range(10)], label = "p5")

plt.legend()
plt.show()