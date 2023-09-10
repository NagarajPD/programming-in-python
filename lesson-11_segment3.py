import threading

class mythread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread is executed',i)

t1=mythread()
t2=mythread()
t1.start()
t2.start()