#binary Search

def binarySearch(values, target):
    left = 0
    right = len(values)-1
    while left <= right:
        mid = (left+right)//2
        if target == values[mid]:
            return mid
        elif target > values[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1