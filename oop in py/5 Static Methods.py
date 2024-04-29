class perform:
    def __init__(self,n):
        self.n=n
    def addition(self,x):
        self.n=self.n+x

    @staticmethod
    def add(a,b): # by using static method you can use function without using self argument
        return a+b

obj=perform(5)
print(obj.n)
obj.addition(10) # class function call
print(obj.n)
print(obj.add(3,4))  #static method function call