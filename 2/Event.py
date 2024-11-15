import logging
import threading
import time
import random

# Configuring logging to track thread activities and interactions
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resource (a list to hold items) and an Event for synchronization
items = []
event = threading.Event()  # Event to signal state changes between threads

# Consumer class representing a thread that consumes items from the shared resource
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            item = items.pop()
            logging.info('Consumer notify: {} popped by {}'.format(item, self.name))

# Producer class representing a thread that produces items for the shared resource
class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Producer notify: item {} appended by {}'.format(item, self.name))
            event.set()
            event.clear()

if __name__ == "__main__":
    t1 = Producer(name='Producer')
    t2 = Consumer(name='Consumer')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# Explanation:
# - A producer-consumer problem using threads and an Event object for synchronization.

