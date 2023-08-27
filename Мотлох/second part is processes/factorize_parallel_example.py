import multiprocessing

def factorize_parallel(number):
    def worker(start, end, number, result):
        for i in range(start, end):
            if number % i == 0:
                result.append(i)
    
    num_cores = multiprocessing.cpu_count()
    chunk_size = number // num_cores
    processes = []
    manager = multiprocessing.Manager()
    result = manager.list()

    for core in range(num_cores):
        start = core * chunk_size + 1
        end = (core + 1) * chunk_size + 1 if core < num_cores - 1 else number + 1
        process = multiprocessing.Process(target=worker, args=(start, end, number, result))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return sorted(result)

a, b, c, d = factorize_parallel(128), factorize_parallel(255), factorize_parallel(99999), factorize_parallel(10651060)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
