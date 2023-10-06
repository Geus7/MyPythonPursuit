def countOne(n):
    count = 0
    for i in range(n + 1):
        count += str(i).count('1')
    return count


n = int(input('Enter the number to count the number of 1s: '))

op = countOne(n)
print("Number of 1s counted:", op)
