# decorators in a method in python which use to print something before and after execution of function
# for example you have function (shop keeper) and have some logic (service) inside it, the function should greet you before and after execution of function soch as "good morining","thanks for using this function"
# decorators just modifies the function

def greet(f): # function in argument
    def mf(*args,**kwargs): # modified functon call
        print("good morning")
        f(*args,**kwargs)
        print("come again")
    return mf

@greet
def hello(name):
    print(f"what whould you like to have, {name}??")

hello("harsh")
