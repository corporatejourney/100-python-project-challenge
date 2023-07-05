import multiprocessing

def worker(num):
    result = num * 2
    print(f"processed:{num} result:{result}")


if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    pool = multiprocessing.Pool(processes =3)
    pool.map(worker,numbers)
    pool.close()
    pool.join()