import numpy as np


# Read number of rows and columns
r, c = map(int, input().split())

elements = []

# Read the array elements row by row
for _ in range(r):
    row = list(map(int, input().split()))
    elements.extend(row)

# Create NumPy array and reshape
arr = np.array(elements).reshape(r, c)

# Display outputs
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
