
from statistics import *


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def bin_ser(arr,goal):
    low,high = 0,len(arr) - 1
    while True:
       
        med = (low + high) // 2
        print(med)
        if arr[med] == goal: return med
        elif arr[med] < goal: low = med + 1
        else: high = med - 1
        if low > high: break
    return -1

print(bin_ser(arr,40))