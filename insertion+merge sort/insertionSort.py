import time

def insertion_sort(A):
    for j in range(1,len(A)):
        
        i = j-1
        key = A[j]
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
