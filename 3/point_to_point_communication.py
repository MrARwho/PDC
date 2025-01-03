from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size 
print(f"My rank is: {rank}")

if rank == 0:
    data = 10000000
    destination_process = 4
    if destination_process < size:  
        comm.send(data, dest=destination_process)
        print(f"Sending data {data} to process {destination_process}")
    else:
        print(f"Invalid destination rank {destination_process}. Only {size} processes are available.")

if rank == 1:
    data = "hello"
    destination_process = 8
    if destination_process < size:  # Ensure the destination process exists
        comm.send(data, dest=destination_process)
        print(f"Sending data '{data}' to process {destination_process}")
    else:
        print(f"Invalid destination rank {destination_process}. Only {size} processes are available.")

if rank == 4:
    data = comm.recv(source=0)
    print(f"Data received is: {data}")

if rank == 8:
    data = comm.recv(source=1)
    print(f"Data received is: {data}")
