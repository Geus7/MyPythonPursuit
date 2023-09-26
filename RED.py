i =int(input("Enter intensity: "))
if i<0 and i<=100:
    print("Invalid Intensity")
else:
    if i >50 and i<=100:
        print(i,"RGB is the Brighest")
    elif i>25 and i<=50:
        print(i,"RGB is dark")
    else:
        print(i,"RGB is light")
