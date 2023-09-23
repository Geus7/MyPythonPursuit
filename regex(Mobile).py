import re
num=input('Enter your number: ')
if re.match('[1-9][0-9]{9}',num):
    print('Number is valid')
else:
    print('Number is invalid')
