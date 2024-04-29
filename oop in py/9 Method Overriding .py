# Method Overriding- changig the methods comming form parents class to child class is called method overriding

class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

#class gol(shape):
#    def __init__(self, r):
#        self.r=r
#    def area(self):
#        return 3.14*self.r*self.r

rec1=shape(2,3)
print(rec1.area())

#c=gol(5)
#print(c.area()) # you are passing 1 argument but area function which is belong to parents class require 2 argument hence it will throw erroe of attribut is missing

# you can use super method the example is written below for circle function

class gol(shape):
    def __init__(self, r):
        self.r=r
        super().__init__(r,r)
    def area(self):
        return 3.14*super().area()
    
obj=gol(3)
print(obj.area())