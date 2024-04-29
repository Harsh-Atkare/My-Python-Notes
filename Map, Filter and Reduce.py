# map
def cube(val):
    return val*val*val

l=[1,2,3,4,5,6,7,8]
print(l)
cubed_list=list(map(cube,l))
print(cubed_list)

#filter
def filter_list(x):
    return x>4
True_list=list(filter(filter_list,l))
print(True_list)