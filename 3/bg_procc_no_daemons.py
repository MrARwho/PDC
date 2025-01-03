#
import multiprocessing
import time
def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'background_process':
        for i in range(0,5):
            print('%d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('%d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    
if __name__ == '__main__':
    bg_proc = multiprocessing.Process(name='bg_proc',target=foo)
    bg_proc.daemon = False

    no_bg_procc = multiprocessing.Process(name='no_bg_procc',target=foo)
    
    no_bg_procc.daemon = False
    
    bg_proc.start()
    no_bg_procc.start()
    

