class myclass:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f"this is value {self.value}")
    @property
    def ten_value(self):
        return 10*self.value
obj1=myclass(10)
print(obj1.ten_value) #getter
obj1.show()