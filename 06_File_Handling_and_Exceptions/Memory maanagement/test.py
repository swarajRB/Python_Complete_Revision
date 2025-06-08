#multiprocessing>> should be used in case of computation
#use case 1:

import multiprocessing

import time
start = time.perf_counter()

def square(index, value):
    value[index] = value[index] ** 2

arr = multiprocessing.Array('i', [1, 2, 5, 3, 40000000000])


processes = []
for i in range(5): #in array 5 nos, therefore loop will be in range(5)
    p = multiprocessing.Process(target = square, args = (i, arr))
    p.start()
    processes.append(p)
    
for process in processes:
    process.join()

print(list(arr))

    

end = time.perf_counter()

print(f"The program finished in {round(end-start, 2)} seconds")