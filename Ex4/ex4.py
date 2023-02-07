import bisect

def binary_search(arr, value):
    index = bisect.bisect_left(arr, value)
    if index != len(arr) and arr[index] == value:
        return index
    else:
        return -1
    
arr = [1, 2, 4, 4, 4, 8, 9]
value = 8

index = binary_search(arr, value)
if index != -1:
    print(f"The first occurence if {value} in {arr} is at index {index}")
else:
    print(f"{value} not found in {arr}")
    
# This program defines a function binary_search that takes a sorted list arr 
# and a value value as input and returns the index of the first occurrence of the value in the list using the bisect_left 
# function from the bisect module. If the value is not found in the list, the function returns -1. 
# Then, it demonstrates the usage of the function by finding the first occurrence of 4 in a sorted list [1, 2, 4, 4, 4, 8, 9].