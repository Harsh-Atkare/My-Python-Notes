class emp:
    company="apple"
    def show(self):
        print(f"the name of emp is {self.name} and comapny is {self.company}")

    @classmethod
    def change_company(self,new_comapny):
        self.company=new_comapny
    

obj1=emp()
obj1.name="harsh"
obj1.show()
obj1.change_company("tcs")
obj1.show()
print(emp.company) # after updating the company name it is still showing old company name which is fine, if you want to chage company name with new one in class then you have to use class method by @classmethod above the change function
obj2=emp()
obj2.name="harsh"
obj2.show()
obj2.change_company("xyz")
obj2.show()
# new for other objects, the comapny name has changed 