weight=int(input("Weight:"))
unit  =input("(k)g or (L)bs: ")
if unit =="k":
    print("weight in Lbs: ",weight/0.45)
else:
    print("Weight in kg: ",weight*0.45)
