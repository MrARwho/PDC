#barrier
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print(f"process {name} : {datetime.fromtimestamp(now)}")

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print(f"process {name} : {datetime.fromtimestamp(now)}")

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='with barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    Process(name='with barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    Process(name='without barrier'\
            ,target=test_without_barrier).start()
    Process(name='without barrier'\
            ,target=test_without_barrier).start()
    


