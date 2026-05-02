# Read array elements
arr = list(map(int, input().split()))

# Read key element
key = int(input().strip())

# Linear search
found = False
for i in range(len(arr)):
    if arr[i] == key:
        print(i)
        found = True
        break

# If not found
if not found:
    print("Not found")
