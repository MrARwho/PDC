import threading

def my_func(thread_number):
    return print('my_func called by thread N°{}'.format(thread_number))

def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()

# Summary: This program creates and starts 10 threads sequentially. Each thread calls the my_func function with its respective thread number and waits for the thread to finish before starting the next one.

