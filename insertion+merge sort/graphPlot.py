import matplotlib.pyplot as plt
import time
import random

from numpy import average
from insertionSort import insertion_sort
from mergeSort import merge_sort


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

    plt.figure("Insertion Sort-Best Case")
    plt.title("Insertion Sort")                                    #title of the graph
    plt.xlabel("Array Size")                                       #x-axis label
    plt.ylabel("Time(in microseconds)")                            #y-axis label
    plt.plot(randomList, bestCaseTime, '*', label="Best Case")     #plotting the best case
    plt.legend()
    plt.figure("Insertion Sort-Worst Case")
    plt.title("Insertion Sort")                                    #title of the graph
    plt.xlabel("Array Size")                                       #x-axis label
    plt.ylabel("Time(in microseconds)")  
    plt.plot(randomList, worstCaseTime, '+', label="Worst Case")   #plotting the worst case
    plt.legend()
    plt.figure("Insertion Sort-Average Case")
    plt.title("Insertion Sort")                                    #title of the graph
    plt.xlabel("Array Size")                                       #x-axis label
    plt.ylabel("Time(in microseconds)")  
    plt.plot(randomList, avgCaseTime, '.', label="Average Case")   #plotting the average case
    plt.legend()

def merge_sort_plot():
    bestCaseTime = []
    worstCaseTime = []

    for num in randomList:
        A = list(range(num))
        B = list(A)
        random.shuffle(B)
        bestCaseStartTime = time.time()
        merge_sort(A,0,len(A)-1)
        bestCaseEndTime = time.time()
        bestCaseTime.append((bestCaseEndTime-bestCaseStartTime)*1000*1000)

    plt.figure("Merge Sort-Best Case")
    plt.title("Merge Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Time(in microseconds)")
    plt.plot(randomList, bestCaseTime, '*', label="Best Case")
    plt.legend()


if __name__ == '__main__':
    merge_sort_plot()
    insertion_sort_plot()
    plt.show()
