#function for geometric mean
'''
def gmean(a,b):
    calculate =(a*b)/(a+b)
    print(calculate)

a=int(input("enter first number"))
b=int(input("enter seccond number"))
gmean(a,b)
'''

# print gretest number
'''
a=int(input("enter first number"))
b=int(input("enter seccond number"))

def greater(a,b):
    if a>b:
        print("{} is greater".format(a))
    else:
        print("{} is greater".format(b))

greater(a,b)
'''
 #arbetry function

def avg(*numbers):
    #here number's type is tuple
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average is - {}".format(sum/len(numbers)))
avg(2,2,4)