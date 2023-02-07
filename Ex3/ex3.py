import bisect

def insert_list(arr, value):
    bisect.insort_left(arr, value)
    return arr

arr = [1, 2, 3, 4, 6, 8, 9]
value = 5

sorted_arr = insert_list(arr, value)
print(f"The sorted list after inserting {value} is: {sorted_arr}")