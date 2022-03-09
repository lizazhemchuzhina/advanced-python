import math
import concurrent
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate(f, a, b, cur_job_num=0, n_jobs=1, n_iter=1000):
    start_time = time.time()
    acc = 0
    step = (b - a) / n_iter
    left, right = n_iter // n_jobs * cur_job_num, min(n_iter, n_iter // n_jobs * (cur_job_num + 1))
    for i in range(left, right):
        acc += f(a + i * step) * step
    log_information = f'Task number: {cur_job_num}, started in time point of: {start_time},' \
                      f' with iterations from {left} to {right}, and accumulated result of:' \
                      f'{acc}\n'
    return acc, log_information


def executor_service(f, a, b, n_jobs, pool_executor, logging_to_file):
    start_time = time.time()
    futures = []
    with pool_executor(max_workers=n_jobs) as executor:
        result = 0
        for i in range(n_jobs):
            futures.append(executor.submit(integrate, f, a, b, i, n_jobs))
        for t in concurrent.futures.as_completed(futures):
            acc, log_information = t.result()
            result += acc
            logging_to_file.write(log_information)
    return time.time() - start_time, result


if __name__ == '__main__':
    cpu_num = multiprocessing.cpu_count()
    with open('artifacts/medium_logs.txt', "w") as logging_to_file, \
            open('artifacts/medium_time.txt', "w") as file:
        for n_jobs in range(1, 2 * cpu_num + 1):
            file.write(f'Task number: {n_jobs}\n')
            threads_time, threads_result = executor_service(math.cos, 0, math.pi / 2, n_jobs, ThreadPoolExecutor,
                                                            logging_to_file)
            file.write(f'Threads: with time: {threads_time} and final result: {threads_result}\n ')
            process_time, process_result = executor_service(math.cos, 0, math.pi / 2, n_jobs, ProcessPoolExecutor,
                                                            logging_to_file)
            file.write(f'Processes with time: {process_time} and final result : {process_result}\n')
