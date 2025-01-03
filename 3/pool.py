import multiprocessing

def function_add(data):
    result = data+data
    return result


if __name__ == '__main__':
    inputs = list(range(0,100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_add, inputs)

    pool.close() 
    pool.join()  
    print ('Pool outputs:', pool_outputs)
    