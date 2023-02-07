import bisect

def binary_search(arr, value):
    index = bisect.bisect_right(arr, value)
    if index != len(arr) + 1 and arr[index - 1] == value:
        return index - 1
    else:
        return -1
    
arr = [1, 2, 3, 4, 8, 10, 12]
value = 8

num_position = binary_search(arr, value)
if num_position == -1:
    print("Not present")
else:
    print(f"Last occurence of {value} is present at {num_position}")