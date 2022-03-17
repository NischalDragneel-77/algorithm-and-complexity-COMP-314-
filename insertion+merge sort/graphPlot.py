import matplotlib.pyplot as plot
import time
import random

from numpy import average
from insertionSort import insertion_sort
from mergeSort import merge_sort

fig, (plt1, plt2) = plot.subplots(nrows=1, ncols=2)

randomList = range(10,1000,10)

def insertion_sort_plot():
    bestCaseTime=[]                                                 #list to store the time taken for best case
    worstCaseTime=[]                                                #list to store the time taken for worst case
    avgCaseTime=[]                                                  #list to store the time taken for average case

    for num in randomList:
        A = list(range(num))
        B = list(reversed(A))
        C = list(A)
        random.shuffle(C)
        bestCaseStartTime = time.time()
        insertion_sort(A)
        bestCaseEndTime = time.time()
        bestCaseTime.append((bestCaseEndTime-bestCaseStartTime)*1000*1000)
        worstCaseStartTime = time.time()
        insertion_sort(B)
        worstCaseEndTime = time.time()
        worstCaseTime.append((worstCaseEndTime-worstCaseStartTime)*1000*1000)
        avgCaseStartTime = time.time()
        insertion_sort(C)
        avgCaseEndTime = time.time()
        avgCaseTime.append((avgCaseEndTime-avgCaseStartTime)*1000*1000)
        print(f"arrayy with elements {len(A)} sorted in {bestCaseEndTime-bestCaseStartTime} seconds")
        print(f"arrayy with elements {len(A)} sorted in {avgCaseEndTime-avgCaseStartTime} seconds")
        print(f"arrayy with elements {len(A)} sorted in {worstCaseEndTime-worstCaseStartTime} seconds")

    plt1.set_title("Insertion Sort")                                #title of the graph
    plt1.set_xlabel("Array Size")                                   #x-axis label
    plt1.set_ylabel("Time(in microseconds)")                        #y-axis label
    plt1.plot(randomList, bestCaseTime, '*', label="Best Case")     #plotting the best case
    plt1.plot(randomList, worstCaseTime, '+', label="Worst Case")   #plotting the worst case
    plt1.plot(randomList, avgCaseTime, '.', label="Average Case")   #plotting the average case
    plt1.legend()

def merge_sort_plot():
    bestCaseTime = []
    worstCaseTime = []
    avgCaseTime=[]                                                  

    for num in randomList:
        A = list(range(num))
        B = list(reversed(A))
        C = list(A)
        bestCaseStartTime = time.time()
        merge_sort(A,0,len(A)-1)
        bestCaseEndTime = time.time()
        bestCaseTime.append((bestCaseEndTime-bestCaseStartTime)*1000*1000)
        worstCaseStartTime = time.time()
        merge_sort(B,0,len(B)-1)
        worstCaseEndTime = time.time()
        worstCaseTime.append((worstCaseEndTime-worstCaseStartTime)*1000*1000)
        avgCaseStartTime = time.time()
        merge_sort(C,0,len(C)-1)
        avgCaseEndTime = time.time()
        avgCaseTime.append((avgCaseEndTime-avgCaseStartTime)*1000*1000)

    plt2.set_title("Merge Sort")
    plt2.set_xlabel("Array Size")
    plt2.set_ylabel("Time(in microseconds)")
    plt2.plot(randomList, bestCaseTime, '*', label="Best Case")
    plt2.plot(randomList, worstCaseTime, '+', label="Worst Case")
    plt2.plot(randomList, avgCaseTime, '.', label="Average Case")   
    plt2.legend()


if __name__ == '__main__':
    merge_sort_plot()
    insertion_sort_plot()
    plot.show()
