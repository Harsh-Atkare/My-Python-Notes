# calling the methods of parents call using child class my super keyward
class parents_c:
    def parents_func(self):
        print("this is parents class statement")

class child_c(parents_c):
    def child_func(slef):
        print("this is child class statement")
        super().parents_func() # the function of parents class will be call by using super keyward
    def parents_func(self):
        print("same same")
        super().parents_func()

child_class_obj=child_c()
child_class_obj.child_func()
child_class_obj.parents_func()