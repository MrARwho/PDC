import threading
import time
import random

class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def adder(box, items):
    print("N{} items to ADD ".format(items))
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("ADDED one item {} item to ADD".format(items))

def remover(box, items):
    print("N° {} items to REMOVE".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("REMOVED one item{} item to REMOVE".format(items))

def main():
    items = 5
    box = Box()

    t1 = threading.Thread(target=adder, args=(box, random.randint(10, 20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

"""
This program simulates two threads: one for adding items and another for removing items from a shared Box resource.
The Box class uses an RLock to ensure thread-safety when accessing or modifying the total_items variable.
The adder and remover threads repeatedly add and remove a random number of items from the Box, simulating a producer-consumer-like scenario.
Each thread waits for 1 second between each operation to simulate real-world delays.
RLocks allow a thread to acquire the lock multiple times.
"""
