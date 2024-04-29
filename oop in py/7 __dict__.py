class person:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job

a=person("harsh",21,"student")
print(a.__dict__) # this attribute return the arguments you have passed to class as dictionary
