# This program uses a barrier to simulate a race between three runners, Huey, Dewey, and Louie.
# Each runner is a separate thread that takes a random amount of time (2-5 seconds) to reach a common finish line.
# The barrier ensures all runners wait at the finish line until everyone arrives.
# Once all runners are there, the program prints that the race is over.
# It shows when each runner reaches the barrier with their name and the time.

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('START RACE!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Race over!')

if __name__ == "__main__":
    main()

