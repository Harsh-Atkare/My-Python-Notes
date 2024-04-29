def example():
    try:
        list=[1,2,34,5]
        a=int(input("enter the indec number"))
        print(list[a])
        return 1
    except:
        print("error:- write integer")
    print("it is excecuted")

b=example()
print(b)

# before using finally keyward is i try to print statement after except keyword without error then the statement wouldnt execute
# finally keyward only use inside the function and after exception handling
# if you return the function still it will execute