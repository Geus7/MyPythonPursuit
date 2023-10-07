
def search(arr, key):
    for i in arr:
        if i == key:
            return f"The key {key} is present"
    return "Not true"

l = []
n = int(input("Enter the number of values: "))
for i in range(0, n):
    val = int(input(f"Enter value {i + 1}: "))
    l.append(val)

k = int(input("Enter the key to search: "))
result = search(l, k)
print(result)
