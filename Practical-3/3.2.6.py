import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
search_result = np.where(array1 == search_value)
print(search_result[0])

# Count occurrences in array1
count_result = np.count_nonzero(array1 == count_value)
print(count_result)

# Broadcasting addition
broadcast_result = array1 + broadcast_value
print(broadcast_result)

# Sort the first array
sorted_array = np.sort(array1)
print(sorted_array)
