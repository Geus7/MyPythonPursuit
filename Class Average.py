count = 0
total = 0
n = int(input("Enter how many marks you want to read: "))

while count < n:
    mark = int(input("Enter mark: "))
    if mark < 0:
        print("Mark should be greater than 0, terminates.")
        break
    total = total + mark
    count += 1
else:
    if n > 0:  
        average = total / n
        print("Average mark is", format(average, "0.2f"))
    else:
        print("No marks were entered.")
