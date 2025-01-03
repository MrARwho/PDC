#
import multiprocessing
import time

def foo():

    process_name = multiprocessing.current_process().name
    print(f"Starting process: {process_name}")

    if process_name == 'background_process':

        for i in range(0, 5):
            print(f"{process_name} ---> {i}")
            time.sleep(1)
    else:

        for i in range(5, 9):
            print(f"{process_name} ---> {i}")
            time.sleep(1)

    print(f"Exiting process: {process_name}")


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True

    non_background_process = multiprocessing.Process(
        name='non_background_process',
        target=foo
    )
    non_background_process.daemon = False

    
    background_process.start()
    non_background_process.start()

    

    
    time.sleep(2)
