a = []
n1 = int(input("Enter the number of elements in sorted array 1: "))
for i in range(0, n1):
    l = int(input("Enter element {}: ".format(i+1))) 
    a.append(l)

b = []
n2 = int(input("Enter the number of elements in sorted array 2: ")) 
for j in range(0, n2):
    l = int(input("Enter element {}: ".format(j+1)))
    b.append(l)
a.sort()
b.sort()

sor = []

def mergesort(arr1, arr2):
    i = j = k = 0
    n1 = len(arr1)
    n2 = len(arr2)
    
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            sor.append(arr1[i])
            i += 1
        else:
            sor.append(arr2[j])
            j += 1
        k += 1

    while i < n1:
        sor.append(arr1[i])
        i += 1
        k += 1

    while j < n2:
        sor.append(arr2[j])
        j += 1
        k += 1

mergesort(a, b)
print("The merged and sorted array is:", sor)
