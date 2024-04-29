'''
print("Hello github")
print("its me",6,8,end="-")
print("harsh")

a=34
b="harsh"
print(str(a)+b)

# bulding calculator
a=int(input("enter first number"))
b=int(input("enter second number"))
print("enter the operator +,_,/")
c=str(input())
if c == "+":
    print("a+b=",a+b)
elif c == "-":
    print("a-b=",a-b)
elif c == "/":
    print("a/b=",a/b)
else:
    print("enter valid operator")
'''
print("hello")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
if timestamp == 19:
    print("goodafternoon")
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
