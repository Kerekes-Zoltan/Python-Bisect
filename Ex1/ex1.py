import bisect

def find_insertion_point(arr, value):
    return bisect.bisect_left(arr, value)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 5

insertion_point = find_insertion_point(arr, value)
print(f"The left insertion point for {value} in {arr} is {insertion_point}")