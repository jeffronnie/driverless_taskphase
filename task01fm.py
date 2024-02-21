n = int(input())
lst = []
dict = {}
count = 0

for i in range(0,n):
    ele = input()

    lst.append(ele)

print(lst)

for i in range(65,91):
    for j in range(0,n):
        check = bool(chr(i) in lst[j] or chr(i+32) in lst[j])
        if check is True:
            count = count + 1
    if count > 0:
        dict[chr(i)] = count
    count = 0

print(dict)
class sSort:
    def selectionSort(lst):
        n = len(lst)
        for i in range(0,n):
            min_index = i
            min_str = lst[i]

            for j in range(i+1,n):
                if lst[min_index] > lst[j]:
                    min_index = j
                    min_str = lst[j]
    
            if min_index != i:
                temp = lst[i]
                lst[i] = lst[min_index]
                lst[min_index] = temp
            
        return(lst)
from sSort import *

class bSearch:
    def binarySearch(lst,str):
        nlst = sSort.selectionSort(lst)
        print(nlst)

        low = 0
        high = len(lst) - 1

        while low <= high:
            mid = low + (high - low)//2

            if str == lst[mid]:
                return mid
            elif str > lst[mid]:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1

n = int(input())
lst = []

for i in range(0,n):
    ele = input()
    lst.append(ele)

str = input()
x = bSearch.binarySearch(lst,str)
if x > -1:
    print("String found at", x)
else:
    print("String not found!")
