import time
from linearSearch import linearSearch

if __name__ == "__main__":
    data = list(range(1,100000000,1))
    t1 = time.time()
    linearSearch(data,99999999)
    t2 = time.time()
    timeUsed = t2 - t1

    print("time used is ", timeUsed , " in seconds:")
