from collections.abc import Callable, Iterable, Mapping
import threading
import random
import time
from typing import Any

class diningPhil(threading.Thread):

    running = True

    def __init__(self, xname, fork_l, fork_r):
        threading.Thread.__init__(self)
        self.name = xname
        self.fork_l = fork_l
        self.fork_r = fork_r

    def run(self):
        while(self.running):
            # time.sleep(random.uniform(1,10))
            time.sleep(4)
            print(self.name," is hungry.")
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork_l, self.fork_r

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print(self.name ," swaps forks")
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()
    
    def dining(self):
        print(self.name," starts eating")
        # time.sleep(random.uniform(2,20))
        time.sleep(4)
        print(self.name, " finishes eating")

def dining_philosopgers():
    forks = [threading.Lock() for n in range(5)]
    name_phil_l = ["1", "2", "3", "4", "5"]
    phils = [diningPhil(name_phil_l[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
    random.seed()
    diningPhil.running=True
    for p in phils:
        p.start()
    time.sleep(30)
    diningPhil.running = False
    print("finished.")

dining_philosopgers()