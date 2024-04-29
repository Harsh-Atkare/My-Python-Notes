class person_data: #it is a class
    name="harsh"
    age=13
    qualification="b-tech"

    def info(self):
        print(f"he is {self.name} and he is {self.age} year old.")

a = person_data() # object creation
print(a.name)
print(a.age)
print(a.qualification)
#a.name="om" # new defination assign
#print(a.name) # using new defination
a.info()


print("-------------------example 2-------------------")
class bank:
    def __init__(self,name,balence=0):
        self.name=name
        self.balence=balence
    def deposit(self,ammount):
        self.balence +=ammount
        print(f"rupees {self.balence} is deposited in your bank")
    def wetdraw(self,ammount):
        if self.balence < ammount:
            print("not sufficient balence")
        else:
            self.balence -=ammount
            print(f"{ammount} is debited, total balence is {self.balence}")
    def balence_check(self):
        print(f"Hello {self.name}, your current balence is {self.balence}")


a=bank("harsh")
a.wetdraw(40)
a.deposit(40)
a.wetdraw(10)
a.balence_check()