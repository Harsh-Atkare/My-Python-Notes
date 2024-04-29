class emp:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.__id2=22

    def show(self):
        print(f"You are {self.name}, and your ID is {self.id}")

class pro(emp):
    def lang(self,language):
        print(f"the language which programmer knows is {language}")
    
emp1=emp("harsh",33)
emp1.show()
print(emp1.name) # publically accessable

print("showing both class with inheritence")
pro_obj=pro("om",11)
pro_obj.show()
pro_obj.lang("python")

# by defult everything is accecable in class of python -----public
# to make any variable private we just need to add double underscore '__' in front of that variable so it will convert in private variaboe

#print(emp1.__id)
# but we can access indirectly
print(emp1._emp__id2) # can access indirectly

# protected access specifier is used by single underscore '_'