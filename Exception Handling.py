a=input("enter the number of which you wants to print table")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except:
    print("oopsss... you only can use integer, not string")
print("printitng the statemeent")