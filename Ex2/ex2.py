import bisect

def find_insertion_point(arr, value):
    return bisect.bisect_right(arr, value)

arr = [1, 2, 4, 6, 8, 9]
value = 1

insertion_point = find_insertion_point(arr, value)
print(f"The right insertion point for {value} in {arr} is {insertion_point}")

# This program defines a function find_insertion_point that takes a sorted list arr and a value 
# value as input and returns the right insertion point of the value in the list using 
# the bisect_right function from the bisect module. Then, it demonstrates the usage of the function 
# by finding the right insertion point of 5 in a sorted list [1, 2, 4, 6, 8, 9].