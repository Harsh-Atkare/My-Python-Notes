# for understanding recursion, we are using factorial algorithm
#factorial(4)=4*3*2*1
#factorial(3)=3*2*1
#factorial(2)=2*1
#factorial(1)=1
#factorial(0)=1

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(3))

# writing program for febonachi series
def fib(a):
    return fib(a-1)+fib
    list=[]
    list.append(b)