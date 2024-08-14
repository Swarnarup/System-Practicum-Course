import threading

def thread_fn(t_no):
    print("this is thread ",t_no)

t = threading.Thread(target=thread_fn, args=(1,))
t2 = threading.Thread(target=thread_fn, args=(2,))

t.start()
t2.start()

t.join()
t2.join()