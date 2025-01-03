# Use MPI Reduce to sum arrays across processes

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

array_size = 10

recvdata = np.zeros(array_size, dtype=int)
senddata = (rank + 1) * np.arange(array_size, dtype=int)

print("process %s sending %s " % (rank, senddata))

comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

if rank == 0:
    print('on task', rank, 'after Reduce: data = ', recvdata)
else:
    print('on task', rank, 'after Reduce: (no data received)')
