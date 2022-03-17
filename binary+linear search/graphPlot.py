import matplotlib.pyplot as plot
import time
from linearSearch import linearSearch
from binarySearch import binarySearch

fig, (plt1, plt2) = plot.subplots(nrows=1, ncols=2)

randomList = (range(100,100000,100))

def linearSearchPlot():
    bestCaseTime=[]              #list to store the time taken for best case
    worstCaseTime=[]             #list to store the time taken for worst case
    for num in randomList:          
        bestCaseStartTime = time.time()
        linearSearch(range(num), 0)
        bestCaseEndTime = time.time()
        bestCaseTime.append((bestCaseEndTime-bestCaseStartTime)*1000*1000)
        worstCaseStartTime = time.time()
        linearSearch(range(num), -5)
        worstCaseEndTime = time.time()
        worstCaseTime.append((worstCaseEndTime-worstCaseStartTime)*1000*1000)

    plt1.set_title("Linear Search")                                 #title of the graph
    plt1.set_xlabel("Array Size")                                   #x-axis label
    plt1.set_ylabel("Time(in microseconds)")                        #y-axis label
    plt1.plot(randomList, bestCaseTime, '*', label="Best Case")     #plotting the best case
    plt1.plot(randomList, worstCaseTime, '.', label="Worst Case")   #plotting the worst case
    plt1.legend()

def binarySearchplot():
    bestCaseTime = []
    worstCaseTime = []
    for num in randomList:
        bestCaseStartTime = time.time()
        binarySearch(range(num), (num-1)//2)
        bestCaseEndTime = time.time()
        bestCaseTime.append((bestCaseEndTime-bestCaseStartTime)*1000*1000)
        worstCaseStartTime = time.time()
        binarySearch(range(num), num)
        worstCaseEndTime = time.time()
        worstCaseTime.append((worstCaseEndTime-worstCaseStartTime)*1000*1000)

    plt2.set_title("Binary Search")
    plt2.set_xlabel("Array Size")
    plt2.set_ylabel("Time(in microseconds)")
    plt2.plot(randomList, bestCaseTime, '.', label="Best Case")
    plt2.plot(randomList, worstCaseTime, '*', label="Worst Case")
    plt2.legend()


if __name__ == '__main__':
    binarySearchplot()
    linearSearchPlot()
    plot.show()
