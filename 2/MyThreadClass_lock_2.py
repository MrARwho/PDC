import threading
import time
import os
from threading import Thread
from random import randint

threadLock = threading.Lock()

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        threadLock.acquire()
        print("---> " + self.name + " running, belonging to process ID " + str(os.getpid()) + "\n")
        threadLock.release()
        time.sleep(self.duration)
        print("---> " + self.name + " over\n")

def main():
    start_time = time.time()
    
    thread1 = MyThreadClass("Thread#1 ", randint(1, 10))
    thread2 = MyThreadClass("Thread#2 ", randint(1, 10))
    thread3 = MyThreadClass("Thread#3 ", randint(1, 10))
    thread4 = MyThreadClass("Thread#4 ", randint(1, 10))
    thread5 = MyThreadClass("Thread#5 ", randint(1, 10))
    thread6 = MyThreadClass("Thread#6 ", randint(1, 10))
    thread7 = MyThreadClass("Thread#7 ", randint(1, 10))
    thread8 = MyThreadClass("Thread#8 ", randint(1, 10))
    thread9 = MyThreadClass("Thread#9 ", randint(1, 10))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    print("End")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

# Summary:
# This program creates 9 threads with random sleep durations and executes them concurrently.
# Each thread tries to acquire a lock before printing its start message, ensuring that the output is synchronized.
# The main thread waits for all the created threads to finish before printing "End" and the execution time.


