import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()

class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        with condition:
            if len(items) == 0:
                logging.info('No items to consume')
                condition.wait()
            items.pop()
            logging.info('Consumed 1 item')
            condition.notify()

    def run(self):
        for _ in range(10):
            time.sleep(2)
            self.consume()

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):
        with condition:
            if len(items) == 5:
                logging.info(f'Items produced {len(items)}. Stopped')
                condition.wait()
            items.append(1)
            logging.info(f'Total items {len(items)}')
            condition.notify()

    def run(self):
        for _ in range(10):
            time.sleep(0.5)
            self.produce()

def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()

# Summary:
# This code implements a producer-consumer scenario using threads in Python.
# A Producer thread adds items to a shared list, and a Consumer thread removes items from it.
# Synchronization is managed using a Condition object, ensuring that the consumer waits when there are no items to consume,
# and the producer waits when the list reaches a specified limit. Logging is used to track thread activities and interactions.

