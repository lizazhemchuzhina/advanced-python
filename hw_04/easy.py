import time
from multiprocessing import Process
from threading import Thread


def fibonacci(n):
    res = [1, 1]
    for i in range(2, n):
        res.append(res[i - 1] + res[i - 2])
    return res


if __name__ == "__main__":
    N = 100000

    start = time.time()
    for _ in range(10):
        fibonacci(N)
    sync_time = time.time() - start

    start = time.time()
    threads = [Thread(target=fibonacci, args=(N,)) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    threads_time = time.time() - start

    start = time.time()
    proc = [Process(target=fibonacci, args=(N,)) for _ in range(10)]
    for process in proc:
        process.start()
    for process in proc:
        process.join()
    proc_time = time.time() - start

    with open('artifacts/easy.txt', "w") as file:
        file.write(f'Sync time: {sync_time} seconds\n')
        file.write(f'Threads time: {threads_time} seconds\n')
        file.write(f'Process time: {proc_time} seconds\n')
