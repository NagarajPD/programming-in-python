import threading as th
import time

class mythread(th.Thread):
    def run(self):
        for i in range(5):
            print(self.getName())
            time.sleep(2)

t1=mythread()
t2=mythread()
t3=mythread()

t1.setName("India")
t2.setName("japan")
t3.setName("Russia")

t1.start()
t1.join()
t2.start()
t3.start()