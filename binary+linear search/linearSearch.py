#linear search
def linearSearch(values,target):
    for index,value in enumerate(values):
        if value == target:
            return index
    return -1
