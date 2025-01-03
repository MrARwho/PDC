
import multiprocessing
import time

def myFunc():
    name = multiprocessing.current_process().name
    print ("Starting = %s \n" %name)
    time.sleep(3)
    print ("Exiting = %s \n" %name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process\
                        (name='xyz process',\
                         target=myFunc)

    process_with_default_name = multiprocessing.Process\
                                (target=myFunc)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
    
