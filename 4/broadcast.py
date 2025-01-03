/*************  ✨ Codeium Command 🌟  *************/
# Broadcast data from root process to all other processes
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None

variable_to_share = comm.bcast(variable_to_share, root=0)
print("process = %d" % rank + " variable shared = %d " % variable_to_share)
/******  27b223b2-c68b-476b-bda8-61ef29ec7bbb  *******/