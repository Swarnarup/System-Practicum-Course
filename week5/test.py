import threading

x =0

def incgl():
    global x
    x+=1
    
def taskofThread():
    for _ in range(1000000):
        incgl()
        
def main():
    t1 = threading.Thread(target = taskofThread)
    t2 = threading.Thread(target = taskofThread)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()
    print("x =", x)