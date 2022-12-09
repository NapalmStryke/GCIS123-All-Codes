import arrays
import time

def binary_search_timer(array,target):
    start_time = time.perf_counter()
    BinarySearch(array,target)
    end_time = time.perf_counter()
    elapsed = start_time - end_time
    return elapsed

def BinarySearch(array, myTarget, upper = None, lower = None):
    if upper == None:
        upper = 0
    if lower == None:
        lower = 0
    if upper > lower: 
        return None
    else: 
        mid = (upper + lower)//2
        if myTarget == array[mid]:
            return array[mid]
        if array[mid] < myTarget:
            return BinarySearch(array, myTarget, mid + 1, lower)
        else:
            return BinarySearch(array,myTarget, upper, mid - 1)
        
        
def main():
    
    
    BinarySearch()    
 
        










