import bisect

def binary_search(arr, value):
    index = bisect.bisect_left(arr, value)
    if index:
        return index - 1
    else:
        return -1
arr = [1, 2, 4, 6, 8, 9]
value = 7

index = binary_search(arr, value)
if index != -1:
    print(f"The largest value smaller than {value} in {arr} is at index {index}")
else:
    print(f"No value smaller than {value} found in {arr}")
    
# This program defines a function binary_search that takes a sorted list arr and a value 
# value as input and returns the index of the largest value smaller than the given value 
# in the list using the bisect_left function from the bisect module. If no value smaller 
# than the given value is found in the list, the function returns -1. 
# Then, it demonstrates the usage of the function by finding the largest value smaller
# than 7 in a sorted list [1, 2, 4, 6, 8, 9].