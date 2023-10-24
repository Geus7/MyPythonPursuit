def insort(list):
 for i in range(1,len(list)):
     cv=list[i]
     position = i
     while position>0 and list[position-1]>cv:
         list[position]=list[position-1]
         position = position -1
 list[position]=cv
list=[34,12,1,2,111,23,33]
insort(list)
print(list)
