a = int(input("Enter the first number a: "))
b = int(input("Enter the second number b: "))
c = int(input("Enter the third number c: "))
if a>b:
    if a>c:
        print ('a is the Greatest with',+a,'as its value')
    else:
        print ('c is the Greatest with',+c,'as its value')
else:
    if b>c:
        print ('b is the Greatest with ',+b,'as its value')
    else:print ('c is the Greatest with ',+c,'as its value')
